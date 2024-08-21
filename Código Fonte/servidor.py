import socket
import json
from conf_acesso import *
#from conexao import *
from threading import Thread

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.bind(("127.0.0.1", 5000))
socket_servidor.listen()
dados = []

dicionario = {}

def exec(socket_cliente, address):
    try:    
        while True:
            #print('\n\n\n entrou no while')
            dados = json.loads(socket_cliente.recv(1024).decode())
            if isinstance(dados, dict):
               pass
            elif isinstance(dados, list):
                pass
            else:
                if dados == "/listar":
                    #print(listar_lease())
                    envio = json.dumps(listar_lease())
                    socket_cliente.sendall(envio.encode())
                elif dados == "/listar_interface":
                    envio = json.dumps(listar_enderecos())
                    socket_cliente.sendall(envio.encode())
    except:
        pass    
        


def main():
    socket_cliente, address = socket_servidor.accept()
    #print('\n\n\n aceitou conexao')
    exec(socket_cliente, address)
    #Thread(target=exec, args=(socket_cliente, address)).start()


if __name__ == "__main__":
    main()