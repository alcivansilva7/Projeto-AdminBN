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


