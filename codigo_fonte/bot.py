# Importando bibliotecas necessárias
import telebot, os
import socket
import json
import time
import logging
from datetime import datetime

credenciais = {}
selecoes = []
logado = False

logging.basicConfig(
    filename='bot_commandos.log', # Endereço e Nome do arquivo de Log
    level=logging.INFO, # Nível de severidade dos Logs
    format='%(asctime)s - %(username)s - %(message)s' # Formado das mensagens do Log
)

#chamando a chave API do BOT que foi armazenada numa variável de ambbiente por segurança
bot = telebot.TeleBot(os.getenv('BOT_CHAVE'))


def abrir_conexao(dados):
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect(("127.0.0.1", 5000))
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
            menu(mensagem)
            
        else:
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
            selecoes.append("/cadastrar_usuario")
            bot.send_message(id_chat, "INFORME O USUARIO DO HOTSPOT:")
            bot.register_next_step_handler(mensagem, usuario_hotspot)
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
            selecoes.append("/apagar_usuario")
            bot.send_message(id_chat, "INFORME O USUARIO DO HOTSPOT A SER APAGADO:")
            bot.register_next_step_handler(mensagem, usuario_apagar)
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


def menu(mensagem):
    id_chat = mensagem.chat.id
    bot.send_message(id_chat, """ESCOLHA A OPÇÃO DESEJADA:
/listar LISTA TODOS OS IPs QUE ESTÃO NO LEASE DO DHCP
/listar_interface  LISTA TODOS OS IPs DAS INTERFACES DE REDE
/cadastrar_usuario CADASTRA UM USUÁRIO NO HOTSPOT
/apagar_usuario    APAGA UM USUÁRIO NO HOTSPOT
/logout            DESCONECTAR USUÁRIO
                             """)

@bot.message_handler(commands=["logout"])
def logout(mensagem):
    id_chat = mensagem.chat.id
    if not credenciais:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
    else:
        dados = ['/logout', credenciais[id_chat]['usuario']]
        retorno = abrir_conexao(dados)
        if retorno:
            bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")
        else:
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
'''def iniciar_bot():
    while True:
        try:
            bot.polling(none_stop=True, timeout=60, long_polling_timeout=30)
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            time.sleep(15)  # Espera 15 segundos antes de tentar novamente

# Inicia o bot
iniciar_bot()'''
bot.polling()