# Importando bibliotecas necessárias
import telebot
import socket
import json


socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("localhost", 5000))

# Aqui informamos a chave API do BOT, essa foi usada apenas como exemplo, a definitiva ainda será criada
CHAVE_API = "7247756639:AAGqOKyr1Hl3OouOZWxXGae9Jz8_Z7fjnh0"
credenciais = {}
selecoes = []
logado = False
bot = telebot.TeleBot(CHAVE_API)


def usuario(mensagem):
    id_chat = mensagem.chat.id
    credenciais[id_chat] = {'usuario':mensagem.text}
    bot.send_message(id_chat, "INFORME A SENHA:")
    bot.register_next_step_handler(mensagem, senha)


def senha(mensagem):
    global logado
    id_chat = mensagem.chat.id
    if id_chat in credenciais:
        credenciais[id_chat]['senha'] = mensagem.text
        dados_combinados = {'id_chat':id_chat,'credenciais':credenciais}
        dados = json.dumps(dados_combinados)
        socket_cliente.sendall(dados.encode())
        logado = json.loads(socket_cliente.recv(4096).decode())
        if logado:
            bot.send_message(id_chat, f"SEJA BEM VINDO(A) {credenciais[id_chat]['usuario']}!")
            menu(mensagem)
            
        else:
            bot.send_message(id_chat, "USUÁRIO OU SENHA INCORRETOS, CLIQUE AQUI PARA INICIAR: /iniciar")