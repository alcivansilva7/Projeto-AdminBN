# Importando bibliotecas necessárias
import telebot
import socket
import json


socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("localhost", 5000))

# Aqui informamos a chave API do BOT, essa foi usada apenas como exemplo, a definitiva ainda será criada
CHAVE_API = "Chave"
credenciais = {}
selecoes = []
logado = False
bot = telebot.TeleBot(CHAVE_API)


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

# Retorna True toda fez que a função for chamada
def iniciar(mensagem):
    return True

# Chama a função default sempre que a função iniciar retornar True, é usada para que o BOT sempre esteja apto a responder o usuário com uma resposta padrão
@bot.message_handler(func=iniciar)
def default(mensagem):
    bot.reply_to(mensagem,"""BEM VINDO AO ADMINBN
VOCÊ DEVE SE AUTENTICAR PRIMEIRO!""")

# chama o objeto BOT para ficar em execução, é responsável por verificar continuamente se o bot está recebendo novas mensagens
bot.polling()