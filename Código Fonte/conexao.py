import sqlite3
#cria um pequeno banco de dados para autenticação
def cria_conexao() -> sqlite3.Connection:
    return sqlite3.connect("Código Fonte//adminbn.db", detect_types=sqlite3.PARSE_DECLTYPES)

#cria a tabela ede usuários no banco de dados se ela não existir
def cria_tabela() -> None:
    with cria_conexao() as conexao:
        conexao.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY NOT NULL, user TEXT NOT NULL,"
                        "password_user TEXT NOT NULL, cadastro TIMESTAMP NOT NULL DEFAULT (DATETIME('NOW', 'LOCALTIME')))")

#verifica se existe o usuario e senha e retorna true se existir e false se não existir
def logar(usuario: str, senha: str):
    with cria_conexao() as conexao:
        conexao.row_factory =  sqlite3.Row
        cur = conexao.execute("SELECT * FROM users WHERE user = ? AND password_user = ?",(usuario,senha,))
        resultado = cur.fetchone()
        if resultado:
            return True
        else:
            return False
        
#insere usuários no banco se a função for chamada
def cadastro():
    with cria_conexao() as conexao:
        cur = conexao.execute("INSERT INTO users (user, password_user)"
        "VALUES('alcivan', '123456')")
    sucesso = False
    return True


if __name__ == "__main__":
   cadastro()
