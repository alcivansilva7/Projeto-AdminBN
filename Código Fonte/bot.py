# Importando bibliotecas necessárias
import telebot, os
import socket
import json

#socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket_cliente.connect(("localhost", 5000))
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

# Retorna True toda fez que a função for chamada
def echo(mensagem):
    id_chat = mensagem.chat.id
    bot.send_message(id_chat, mensagem.text)


def iniciar(mensagem):
    return True

# Chama a função default sempre que a função iniciar retornar True, é usada para que o BOT sempre esteja apto a responder o usuário com uma resposta padrão
@bot.message_handler(func=iniciar)
def default(mensagem):
    id_chat = mensagem.chat.id
    bot.reply_to(mensagem,"""BEM VINDO AO ADMINBN
VOCÊ DEVE SE AUTENTICAR PRIMEIRO!""")
    bot.send_message(id_chat, "DIGITE ALGO")
    bot.register_next_step_handler(mensagem, echo)
    

# chama o objeto BOT para ficar em execução, é responsável por verificar continuamente se o bot está recebendo novas mensagens
bot.polling()