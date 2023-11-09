import sqlite3
import os

try:
    import sqlite3
except ImportError:
    print("Erro ao importar o módulo sqlite3")

# Conectar ao banco de dados ou criar um novo arquivo de banco de dados se ele não existir
conn = sqlite3.connect('Database/store.db')
c = conn.cursor()

def limpar_tela():
    os.system('clear' or 'cls')

# Classe para mostrar os dados
class mostrar:
    def __init__(self):
        pass

def buscar_produto_por_nome(nome):
    limpar_tela()
    if nome:  # Verifica se o campo de pesquisa não está vazio
        c.execute("SELECT * FROM inventory WHERE name=?", (nome,))
    else:
        c.execute("SELECT * FROM inventory")
    data = c.fetchall()

    if data:
        for row in data:
            print(f"ID: {row[0]}, Nome: {row[1]}, Preço de Compra: {row[2]}, Preço de Venda: {row[3]}, Estoque: {row[4]}, Lucro: {row[7]}")
    else:
        if nome:
            print(f"Produto com nome '{nome}' não encontrado.")
        else:
            print("Nenhum produto encontrado.")

# Exemplo de pesquisa por nome do produto
nome_produto = input("Digite o nome do produto que deseja pesquisar (pressione Enter para mostrar todos :): ")
buscar_produto_por_nome(nome_produto)

# Fechar a conexão com o banco de dados
conn.close()
