import sqlite3
#cria um pequeno banco de dados para autenticação
def cria_conexao() -> sqlite3.Connection:
    return sqlite3.connect("adminbn.db", detect_types=sqlite3.PARSE_DECLTYPES)