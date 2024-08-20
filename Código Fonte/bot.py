# Importando bibliotecas necessárias
import telebot, os
import socket
import json

socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("localhost", 5000))
credenciais = {}
selecoes = []
logado = False
#chamando a chave API do BOT que foi armazenada numa variável de ambbiente por segurança
bot = telebot.TeleBot(os.getenv('BOT_CHAVE'))

# Autenticação futura

#def usuario(mensagem):
#    id_chat = mensagem.chat.id
#    credenciais[id_chat] = {'usuario':mensagem.text}
#    bot.send_message(id_chat, "INFORME A SENHA:")
#    bot.register_next_step_handler(mensagem, senha)


# Autenticação futura

#def senha(mensagem):
#    global logado
#    id_chat = mensagem.chat.id
#    if id_chat in credenciais:
#        credenciais[id_chat]['senha'] = mensagem.text
#        dados_combinados = {'id_chat':id_chat,'credenciais':credenciais}
#        dados = json.dumps(dados_combinados)
#        socket_cliente.sendall(dados.encode())
#        logado = json.loads(socket_cliente.recv(4096).decode())
#        if logado:
#            bot.send_message(id_chat, f"SEJA BEM VINDO(A) {credenciais[id_chat]['usuario']}!")
#            menu(mensagem)
#            
#        else:
#            bot.send_message(id_chat, "USUÁRIO OU SENHA INCORRETOS, CLIQUE AQUI PARA INICIAR: /iniciar")

#Criando Menu de funcionalidades iniciais do BOT

#função listar ips do lease do DHCP, quando o usuario clica em /listar ele chama essa função.
@bot.message_handler(commands=["listar"])
def listar_ips(mensagem):
    id_chat = mensagem.chat.id
    global logado
    if logado:
        dados = json.dumps("/listar")
        socket_cliente.sendall(dados.encode())
        retorno = json.loads(socket_cliente.recv(4096).decode())
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
    global logado
    if logado:
        dados = json.dumps("/listar_interface")
        socket_cliente.sendall(dados.encode())
        retorno = json.loads(socket_cliente.recv(4096).decode())
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
    global logado
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
    envio = json.dumps(selecoes)
    socket_cliente.sendall(envio.encode())
    retorno = json.loads(socket_cliente.recv(4096).decode())

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
    global logado
    if logado:
        selecoes.append("/apagar_usuario")
        bot.send_message(id_chat, "INFORME O USUARIO DO HOTSPOT A SER APAGADO:")
        bot.register_next_step_handler(mensagem, usuario_apagar)
    else:
        bot.send_message(id_chat, "VOCÊ NÃO ESTÁ LOGADO! CLIQUE AQUI PARA INICIAR: /iniciar")

def usuario_apagar(mensagem):
    id_chat = mensagem.chat.id
    selecoes.append(mensagem.text)
    envio = json.dumps(selecoes)
    socket_cliente.sendall(envio.encode())
    retorno = json.loads(socket_cliente.recv(4096).decode())
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
                             """)



# Retorna True toda fez que a função for chamada
def iniciar(mensagem):
    return True

# Chama a função default sempre que a função iniciar retornar True, é usada para que o BOT sempre esteja apto a responder o usuário com uma resposta padrão
@bot.message_handler(func=iniciar)
def default(mensagem):
    id_chat = mensagem.chat.id
    bot.reply_to(mensagem,"""BEM VINDO AO ADMINBN
VOCÊ DEVE SE AUTENTICAR PRIMEIRO!""")
    #bot.send_message(id_chat, "DIGITE ALGO")
    #bot.register_next_step_handler(mensagem, echo)

    

# chama o objeto BOT para ficar em execução, é responsável por verificar continuamente se o bot está recebendo novas mensagens
bot.polling()

