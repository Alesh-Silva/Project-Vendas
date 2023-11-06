import sqlite3
'''Coneção com o banco de dados'''
    conn = sqlite3.connect('DataBase/Dados.db')
    c = conn.cursor()
    result = c.execute('SELECT MAX(id) from dados')
    for d in result:
        id = d [0]

class Database:
    def __init__(self):
        pass