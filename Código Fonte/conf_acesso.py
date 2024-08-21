import paramiko
import re
import os

dados = []
info = []
def acesso(comandos):
    host = os.getenv('HOST_MIKROTIK')
    username = os.getenv('USER_MIKROTIK')
    password = os.getenv('PASSWORD_MIKROTIK')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(comandos)
    linhas = stdout.readlines()
    stdin.close()
    ssh.close()
    if not linhas:
        return "comando realizado com sucesso"
    else:
        return linhas

def cadastrar_hotspot(usuario,senha):
    comando = f'ip hotspot user add server=hotspot1 name={usuario} password={senha} profile=default'
    return acesso(comando)

def remover_hotspot(usuario):
    comando = f'ip hotspot user remove {usuario}'
    return acesso(comando)

def listar_lease():
    dados.clear()
    comando = 'ip dhcp-server lease print'
    retono = acesso(comando)
    for i in retono:
        texto = i.replace("\n","")
        texto = texto.replace("\r","")
        ips = re.findall(r'\b\d{1,3}(?:\.\d{1,3}){3}\b', texto)
        for u in ips:
            dados.append(u)
    return dados

def listar_enderecos():
    info.clear()
    dados.clear()
    comando = 'ip address print'
    retorno = acesso(comando)
    for i in retorno:
        texto = i.replace("\n","")
        texto = texto.replace("\r","")
        ips = re.findall(r'\s*\d+\s+[A-Z]*\s*([\d\.\/]+)\s+([\d\.]+)\s+(.+?)\s*$', texto)
        for u in ips:
            dados.append(u)
    headers = ["ENDEREÇO", "REDE", "INTERFACE"]
    col_widths = [len(header) for header in headers]
    for row in dados:
        for i, col in enumerate(row):
            col_widths[i] = max(col_widths[i], len(col))
    def print_row(row, col_widths):
        info.append(" | ".join(col.ljust(width) for col, width in zip(row, col_widths)))
    print_row(headers, col_widths)
    #print("-+-".join('-' * width for width in col_widths))
    saida = "-+-".join('-' * width for width in col_widths)
    for row in dados:
        print_row(row, col_widths)
    return info