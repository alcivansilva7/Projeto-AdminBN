import sqlite3
from datetime import datetime, timedelta
#cria um pequeno banco de dados para autenticação
def cria_conexao() -> sqlite3.Connection:
    return sqlite3.connect("adminbn.db", detect_types=sqlite3.PARSE_DECLTYPES)

#cria a tabela ede usuários no banco de dados se ela não existir
def cria_tabela() -> None:
    with cria_conexao() as conexao:
        conexao.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY NOT NULL, user TEXT NOT NULL,"
                        "password_user TEXT NOT NULL, logado BOLLEAN DEFAULT 0, nivel INT NOT NULL, tempo_login TIMESTAMP, cadastro TIMESTAMP NOT NULL DEFAULT (DATETIME('NOW', 'LOCALTIME')))")

#verifica se existe o usuario e senha e retorna true se existir e false se não existir
def logar(usuario: str, senha: str):
    with cria_conexao() as conexao:
        conexao.row_factory =  sqlite3.Row
        cur = conexao.execute("SELECT * FROM users WHERE user = ? AND password_user = ?",(usuario,senha,))
        resultado = cur.fetchone()
        if resultado:
            tempo_login = datetime.now()
            conexao.execute("UPDATE users SET logado=1, tempo_login=? WHERE id=?", (tempo_login, resultado[0]))
            return True
        else:
            return False

def verifica_login(usuario):
    with cria_conexao() as conexao:
        conexao.row_factory = sqlite3.Row
        cur = conexao.execute("SELECT logado, tempo_login FROM users WHERE user=?",(usuario,))
        resultado = cur.fetchone()
        if resultado:
            logado, tempo_login = resultado
            if logado == 1:
                if isinstance(tempo_login, str):
                    tempo_login = datetime.strptime(tempo_login, "%Y-%m-%d %H:%M:%S")
                if datetime.now() - tempo_login < timedelta(minutes=5):
                    return True
                else:
                    logout(usuario)
                    return False
            else:
                return False
        else:
            return False

def logout(usuario):
    with cria_conexao() as conexao:
        conexao.row_factory =  sqlite3.Row
        cur = conexao.execute("UPDATE users SET logado=0 WHERE user=?",(usuario,))
        return True

#insere usuários no banco se a função for chamada
def cadastro():
    with cria_conexao() as conexao:
        cur = conexao.execute("INSERT INTO users (user, password_user, nivel)"
        "VALUES('mizael', '123456','1')")
    return True


if __name__ == "__main__":
    pass