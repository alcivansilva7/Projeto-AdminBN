import socket
import json
from conf_acesso import *
from conexao import *
from threading import Thread

def cliente(socket_cliente):
    try:
        dados = json.loads(socket_cliente.recv(1024).decode())

        if isinstance(dados, dict):
            id_chat = dados['id_chat']
            retorno = logar(dados['credenciais'][str(id_chat)]['usuario'], dados['credenciais'][str(id_chat)]['senha'])
            envio = json.dumps(retorno)
            socket_cliente.sendall(envio.encode())

        elif isinstance(dados, list):
            if dados[0] == "/cadastrar_usuario":
                envio = json.dumps(cadastrar_hotspot(dados[1], dados[2]))
                socket_cliente.sendall(envio.encode())
            elif dados[0] == "/apagar_usuario":
                envio = json.dumps(remover_hotspot(dados[1]))
                socket_cliente.sendall(envio.encode())
            elif dados[0] == "/logout":
                envio = json.dumps(logout(dados[1]))
                socket_cliente.sendall(envio.encode())
            elif dados[0] == "/verificar":
                envio = json.dumps(verifica_login(dados[1]))
                socket_cliente.sendall(envio.encode())
                
        else:
            if dados == "/listar":
                envio = json.dumps(listar_lease())
                socket_cliente.sendall(envio.encode())
            elif dados == "/listar_interface":
                envio = json.dumps(listar_enderecos())
                socket_cliente.sendall(envio.encode())
                
    finally:
        socket_cliente.close()

def exec():
    socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_servidor.bind(("0.0.0.0", 5000))
    socket_servidor.listen()
    
    while True:
        socket_cliente, address = socket_servidor.accept()
        Thread(target=cliente, args=(socket_cliente,)).start()

def main():
    try:
        thread_exec = Thread(target=exec)
        thread_exec.start()
        thread_exec.join()  # Aguarda até que a thread principal termine
    except KeyboardInterrupt:
        print("\nServidor encerrado.")

if __name__ == "__main__":
    main()