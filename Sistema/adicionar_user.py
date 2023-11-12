import sqlite3

try:
    import sqlite3
except ImportError:
    print("Erro ao importar o módulo sqlite3")
# Conectar ao banco de dados ou criar um novo arquivo de banco de dados se ele não existir
conn = sqlite3.connect('Database/security.db')
c = conn.cursor()
