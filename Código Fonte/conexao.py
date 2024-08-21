import sqlite3
#cria um pequeno banco de dados para autenticação
def cria_conexao() -> sqlite3.Connection:
    return sqlite3.connect("adminbn.db", detect_types=sqlite3.PARSE_DECLTYPES)

#cria a tabela ede usuários no banco de dados se ela não existir
def cria_tabela() -> None:
    with cria_conexao() as conexao:
        conexao.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY NOT NULL, user TEXT NOT NULL,"
                        "password_user TEXT NOT NULL, cadastro TIMESTAMP NOT NULL DEFAULT (DATETIME('NOW', 'LOCALTIME')))")
