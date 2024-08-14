# Importando bibliotecas necessárias
import telebot
import socket
import json


socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_cliente.connect(("localhost", 5000))

