# Importando bibliotecas necessárias
import telebot, os
import socket
import json
import time
import logging
from datetime import datetime

credenciais = {}
selecoes = []

logging.basicConfig(
    filename='bot_commandos.log', # Endereço e Nome do arquivo de Log
    level=logging.INFO, # Nível de severidade dos Logs
    format='%(asctime)s - %(username)s - %(message)s' # Formado das mensagens do Log
)

#chamando a chave API do BOT que foi armazenada numa variável de ambbiente por segurança
bot = telebot.TeleBot(os.getenv('BOT_CHAVE'))


def abrir_conexao(dados):
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect(("servidor", 5000))
    dados = json.dumps(dados)
    socket_cliente.sendall(dados.encode())
    dados = json.loads(socket_cliente.recv(4096).decode())
    socket_cliente.close()
    return dados

# Função para registrar o log dos comandos
def registrar_log(username, comando):
    logging.info(f'Comando executado: {comando}', extra={'username': username})




#função que solicita a senha do usuário para a autenticação.
def usuario(mensagem):
    id_chat = mensagem.chat.id
    credenciais[id_chat] = {'usuario':mensagem.text}
    bot.delete_message(id_chat,mensagem.message_id)
    bot.send_message(id_chat, "INFORME A SENHA:")
    bot.register_next_step_handler(mensagem, senha)

#função que verifica e loga o usuário
def senha(mensagem):
    id_chat = mensagem.chat.id
    if id_chat in credenciais:
        credenciais[id_chat]['senha'] = mensagem.text
        dados_combinados = {'id_chat':id_chat,'credenciais':credenciais}
        bot.delete_message(id_chat,mensagem.message_id)
        logado = abrir_conexao(dados_combinados)
        if logado:
            logging.info(f'Usuário {credenciais[id_chat]["usuario"]} se autenticou com sucesso.', extra={'username': credenciais[id_chat]['usuario']})
            menu(mensagem)
            
        else:
            logging.warning(f'Tentativa de login com usuário {credenciais[id_chat]["usuario"]}', extra={'username': credenciais[id_chat]['usuario']})
            bot.send_message(id_chat, "USUÁRIO OU SENHA INCORRETOS, CLIQUE AQUI PARA INICIAR: /iniciar")


#função listar ips do lease do DHCP, quando o usuario clica em /listar ele chama essa função.
@bot.message_handler(commands=["listar"])
def listar_ips(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/verificar', credenciais[id_chat]['usuario']]
        logado = abrir_conexao(dados)
        if logado:
            dados2 = ['/nivel', credenciais[id_chat]['usuario']]
            verifica_nivel = abrir_conexao(dados2)
            if 1 <= verifica_nivel[0]:
                dados = "/listar"
                retorno = abrir_conexao(dados)
                registrar_log(credenciais[id_chat]['usuario'], dados)
                if not retorno:
                    bot.send_message(id_chat, "PARECE QUE HOUVE UM ERRO")
                    menu(mensagem)
                else:
                    saida = "\n".join(retorno)
                    bot.send_message(id_chat, saida)
                    menu(mensagem)
            else:
                bot.send_message(id_chat, "VOCÊ NÃO TEM PERMISSÃO PRA ACESSAR ESSA FUNÇÃO!")
                menu(mensagem)
        else:
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")


#função listar ips das interfaces, quando o usuario clica em /listar_interface ele chama essa função.
@bot.message_handler(commands=["listar_interface"])
def listar_interface(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/verificar', credenciais[id_chat]['usuario']]
        logado = abrir_conexao(dados)
        if logado:
            dados2 = ['/nivel', credenciais[id_chat]['usuario']]
            verifica_nivel = abrir_conexao(dados2)
            if 1 <= verifica_nivel[0]:
                dados = "/listar_interface"
                retorno = abrir_conexao(dados)
                registrar_log(credenciais[id_chat]['usuario'], dados)
                if not retorno:
                    bot.send_message(id_chat, "PARECE QUE HOUVE UM ERRO")
                    menu(mensagem)
                else:
                    saida = "\n".join(retorno)
                    bot.send_message(id_chat, saida)
                    menu(mensagem)
            else:
                bot.send_message(id_chat, "VOCÊ NÃO TEM PERMISSÃO PRA ACESSAR ESSA FUNÇÃO!")
                menu(mensagem)
        else:
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")


#função cadastrar usuário no hotspost, quando o usuario clica em /cadastrar_usuário ele chama essa função.
@bot.message_handler(commands=["cadastrar_usuario"])
def cadastrar_usuario(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/verificar', credenciais[id_chat]['usuario']]
        logado = abrir_conexao(dados)
        if logado:
            dados2 = ['/nivel', credenciais[id_chat]['usuario']]
            verifica_nivel = abrir_conexao(dados2)
            if 2 <= verifica_nivel[0]:
                selecoes.append("/cadastrar_usuario")
                bot.send_message(id_chat, "INFORME O USUARIO DO HOTSPOT:")
                bot.register_next_step_handler(mensagem, usuario_hotspot)
            else:
                bot.send_message(id_chat, "VOCÊ NÃO TEM PERMISSÃO PRA ACESSAR ESSA FUNÇÃO!")
                menu(mensagem)
        else:
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")

def usuario_hotspot(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    bot.send_message(id_chat, "INFORME A SENHA DO HOTSPOT:")
    bot.register_next_step_handler(mensagem, senha_hotspot)

def senha_hotspot(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    retorno = abrir_conexao(selecoes)
    registrar_log(credenciais[id_chat]['usuario'], selecoes[0])
    if retorno == "comando realizado com sucesso":
        bot.send_message(id_chat, "USUARIO CADASTRADO COM SUCESSO!")
        menu(mensagem)
    else:
        bot.send_message(id_chat, "USUÁRIO JÁ EXISTE!")
        menu(mensagem)
    selecoes.clear()


#função apagar usuário no hotspost, quando o usuario clica em /apgar_usuário ele chama essa função.
@bot.message_handler(commands=["apagar_usuario"])
def apagar_usuario(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/verificar', credenciais[id_chat]['usuario']]
        logado = abrir_conexao(dados)
        if logado:
            dados2 = ['/nivel', credenciais[id_chat]['usuario']]
            verifica_nivel = abrir_conexao(dados2)
            if 2 <= verifica_nivel[0]:
                selecoes.append("/apagar_usuario")
                bot.send_message(id_chat, "INFORME O USUARIO DO HOTSPOT A SER APAGADO:")
                bot.register_next_step_handler(mensagem, usuario_apagar)
            else:
                bot.send_message(id_chat, "VOCÊ NÃO TEM PERMISSÃO PRA ACESSAR ESSA FUNÇÃO!")
                menu(mensagem)
        else:
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")

def usuario_apagar(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    retorno = abrir_conexao(selecoes)
    registrar_log(credenciais[id_chat]['usuario'], selecoes[0])
    if retorno == "comando realizado com sucesso":
        bot.send_message(id_chat, "USUARIO APAGADO COM SUCESSO!")
        menu(mensagem)
    else:
        bot.send_message(id_chat, "USUÁRIO INEXISTENTE!")
        menu(mensagem)
    selecoes.clear()

'''def menu2(mensagem):
    id_chat = mensagem.chat.id
    bot.send_message(id_chat, """ESCOLHA A OPÇÃO DESEJADA:
/listar LISTA TODOS OS IPs QUE ESTÃO NO LEASE DO DHCP
/listar_interface  LISTA TODOS OS IPs DAS INTERFACES DE REDE
/cadastrar_usuario CADASTRA UM USUÁRIO NO HOTSPOT
/apagar_usuario    APAGA UM USUÁRIO NO HOTSPOT
/logout            DESCONECTAR USUÁRIO
                             """)'''
#cria um menu dinâmico de acordo com a permissão do usuário
def menu(mensagem):
    id_chat = mensagem.chat.id
    dic_menu = {"/listar":{'desc':'LISTA TODOS OS IPs QUE ESTÃO NO LEASE DO DHCP', 'nivel':1},
                "/listar_interface":{'desc':'LISTA TODOS OS IPs DAS INTERFACES DE REDE', 'nivel':1},
                "/cadastrar_usuario":{'desc':'CADASTRA UM USUÁRIO NO HOTSPOT', 'nivel':2},
                "/apagar_usuario":{'desc':'APAGA UM USUÁRIO NO HOTSPOT', 'nivel':2},
                "/bot_cadastrar":{'desc':'CADASTRA UM USUÁRIO DO BOT', 'nivel':3},
                "/bot_apagar":{'desc':'APAGA UM USUÁRIO DO BOT', 'nivel':3},
                "/bot_permissao":{'desc':'ATUALIZA A PERMISSÃO DE UM USUÁRIO DO BOT', 'nivel':3},
                "/logout":{'desc':'DESCONECTAR USUÁRIO', 'nivel':1}}
    envio = ["/nivel", credenciais[id_chat]['usuario']]
    retorno = abrir_conexao(envio)
    filtro = dict(filter(lambda item: item[1]['nivel'] <= retorno[0], dic_menu.items()))
    menu = '\n'.join(f"""{chave}  {descricao['desc']}""" for chave, descricao in filtro.items())
    menu_final = "ESCOLHA A OPÇÃO DESEJADA:\n\n"+ menu
    bot.send_message(id_chat,menu_final)

@bot.message_handler(commands=["bot_cadastrar"])
def bot_cadastrar(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/verificar', credenciais[id_chat]['usuario']]
        logado = abrir_conexao(dados)
        if logado:
            dados2 = ['/nivel', credenciais[id_chat]['usuario']]
            verifica_nivel = abrir_conexao(dados2)
            if 3 <= verifica_nivel[0]:
                selecoes.append("/bot_cadastrar")
                bot.send_message(id_chat, "INFORME O USUÁRIO DO BOT A SER CADASTRADO:")
                bot.register_next_step_handler(mensagem, usuario_bot_cadastrar)
            else:
                bot.send_message(id_chat, "VOCÊ NÃO TEM PERMISSÃO PRA ACESSAR ESSA FUNÇÃO!")
                menu(mensagem)
        else:
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")

def usuario_bot_cadastrar(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    bot.delete_message(id_chat,mensagem.message_id)
    bot.send_message(id_chat, "INFORME A SENHA DO USUÁRIO DO BOT A SER CADASTRADO:")
    bot.register_next_step_handler(mensagem, senha_bot_cadastrar)

def senha_bot_cadastrar(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    bot.delete_message(id_chat,mensagem.message_id)
    bot.send_message(id_chat, "INFORME O NIVEL DE PERMISSÃO DO USUÁRIO DO BOT A SER CADASTRADO(1-3):")
    bot.register_next_step_handler(mensagem, nivel_bot_cadastrar)

def nivel_bot_cadastrar(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    bot.delete_message(id_chat,mensagem.message_id)
    if int(selecoes[3]) in range(1,4):
        retorno = abrir_conexao(selecoes)
        if retorno:
            bot.send_message(id_chat, "USUÁRIO CADASTRADO COM SUCESSO!")
            menu(mensagem)
        else:
            bot.send_message(id_chat, "USUÁRIO JÁ EXISTE!")
            menu(mensagem)
        selecoes.clear()
    else:
        selecoes.clear()
        bot.send_message(id_chat, "O NIVEL DE PERMISSÃO INFORMADO NÃO É VÁLIDO!")
        bot_cadastrar(mensagem)


@bot.message_handler(commands=["bot_apagar"])
def bot_apagar(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/verificar', credenciais[id_chat]['usuario']]
        logado = abrir_conexao(dados)
        if logado:
            dados2 = ['/nivel', credenciais[id_chat]['usuario']]
            verifica_nivel = abrir_conexao(dados2)
            if 3 <= verifica_nivel[0]:
                selecoes.append("/bot_apagar")
                bot.send_message(id_chat, "INFORME O USUÁRIO DO BOT A SER APAGADO:")
                bot.register_next_step_handler(mensagem, usuario_bot_apagar)
            else:
                bot.send_message(id_chat, "VOCÊ NÃO TEM PERMISSÃO PRA ACESSAR ESSA FUNÇÃO!")
                menu(mensagem)
        else:
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")

def usuario_bot_apagar(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    bot.delete_message(id_chat,mensagem.message_id)
    retorno = abrir_conexao(selecoes)
    if retorno:
        bot.send_message(id_chat, "USUÁRIO APAGADO COM SUCESSO!")
        menu(mensagem)
    else:
        bot.send_message(id_chat, "USUÁRIO NÃO EXISTE OU JÁ FOI EXCLUÍDO!")
        menu(mensagem)
    selecoes.clear()


@bot.message_handler(commands=["bot_permissao"])
def bot_permissao(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/verificar', credenciais[id_chat]['usuario']]
        logado = abrir_conexao(dados)
        if logado:
            dados2 = ['/nivel', credenciais[id_chat]['usuario']]
            verifica_nivel = abrir_conexao(dados2)
            if 3 <= verifica_nivel[0]:
                selecoes.append("/bot_permissao")
                bot.send_message(id_chat, "INFORME O USUÁRIO DO BOT A SER MUDADA A PERMISSÃO:")
                bot.register_next_step_handler(mensagem, usuario_bot_permissao)
            else:
                bot.send_message(id_chat, "VOCÊ NÃO TEM PERMISSÃO PRA ACESSAR ESSA FUNÇÃO!")
                menu(mensagem)
        else:
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")

def usuario_bot_permissao(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    bot.delete_message(id_chat,mensagem.message_id)
    bot.send_message(id_chat, "INFORME O NOVO NÍVEL DO USUÁRIO(1-3):")
    bot.register_next_step_handler(mensagem, usuario_bot_nivel)

def usuario_bot_nivel(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    bot.delete_message(id_chat,mensagem.message_id)
    if int(selecoes[2]) in range(1,4):
        retorno = abrir_conexao(selecoes)
        if retorno:
            bot.send_message(id_chat, "PERMISSÃO ALTERADA COM SUCESSO!")
            menu(mensagem)
        else:
            bot.send_message(id_chat, "USUÁRIO INEXISTENTE!")
            menu(mensagem)
        selecoes.clear()
    else:
        selecoes.clear()
        bot.send_message(id_chat, "O NIVEL DE PERMISSÃO INFORMADO NÃO É VÁLIDO!")
        bot_permissao(mensagem)

@bot.message_handler(commands=["logout"])
def logout(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/logout', credenciais[id_chat]['usuario']]
        retorno = abrir_conexao(dados)
        if retorno:
            logging.info(f'Usuário {credenciais[id_chat]["usuario"]} fez logout com sucesso.', extra={'username': credenciais[id_chat]['usuario']})
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
        else:
            logging.error(f'Houve um erro ao tentar fazer logout do usuário {credenciais[id_chat]["usuario"]}.', extra={'username': credenciais[id_chat]['usuario']})
            bot.send_message(id_chat, "HOUVE UM ERRO AO FAZER O LOGOUT")

# Retorna True toda fez que a função for chamada
def iniciar(mensagem):
    return True

# Chama a função default sempre que a função iniciar retornar True, é usada para que o BOT sempre esteja apto a responder o usuário com uma resposta padrão e solicitar autenticação
@bot.message_handler(func=iniciar)
def default(mensagem):
    id_chat = mensagem.chat.id
    bot.reply_to(mensagem,"""BEM VINDO AO ADMINBN
VOCÊ DEVE SE AUTENTICAR PRIMEIRO!""")
    bot.send_message(mensagem.chat.id, "INFORME O USUÁRIO:")
    bot.register_next_step_handler(mensagem, usuario)

# chama o objeto BOT para ficar em execução, é responsável por verificar continuamente se o bot está recebendo novas mensagens
def iniciar_bot():
    while True:
        try:
            bot.polling(none_stop=True, timeout=60, long_polling_timeout=30)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            time.sleep(15)  # Espera 15 segundos antes de tentar novamente

# Inicia o bot
iniciar_bot()
#bot.polling()