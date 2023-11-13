import sqlite3
import os

def buscar_produto(conn, nome):
    def limpar_tela():
        os.system('clear' or 'cls')

    limpar_tela()

    c = conn.cursor()

    if nome:  # Verifica se o campo de pesquisa não está vazio
        c.execute("SELECT * FROM inventory WHERE name=?", (nome,))
    else:
        c.execute("SELECT * FROM inventory")

    data = c.fetchall()

    if data:
        for row in data:
            print(f"ID: {row[0]}, Nome: \033[32m{row[1]}\033[0m, Preço de Compra: {row[2]}, Preço de Venda: {row[3]}, Estoque: {row[4]}, Lucro: {row[7]}")
    else:
        if nome:
            print(f"Produto com nome '{nome}' não encontrado.")
        else:
            print("Nenhum produto encontrado.")
    
    c.close()

if __name__ == "__main__":
    try:
        import sqlite3
    except ImportError:
        print("Erro ao importar o módulo sqlite3")

    # Conectar ao banco de dados ou criar um novo arquivo de banco de dados se ele não existir
    conn = sqlite3.connect('Database/store.db')

    # Exemplo de pesquisa por nome do produto
    nome_produto = input("Digite o nome do produto que deseja pesquisar (pressione Enter para mostrar todos :) ")
    buscar_produto(conn, nome_produto)

    # Fechar a conexão com o banco de dados
    conn.close()
