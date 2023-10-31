import sqlite3

# Função para criar a tabela de produtos
def criar_tabela_produtos():
    conn = sqlite3.connect("sistema_vendas.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            preco REAL,
            estoque INTEGER
        )
    """)
    conn.commit()#confirma a modificação da tabela
    conn.close()

# Função para adicionar um novo produto
def adicionar_produto(nome, preco, estoque):
    conn = sqlite3.connect("sistema_vendas.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", (nome, preco, estoque))
    conn.commit()#confirma a modificação da tabela
    conn.close()

# Função para listar todos os produtos
def listar_produtos():
    conn = sqlite3.connect("sistema_vendas.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()#retorna as linhas do resultado da consulta em uma lista, em vez de um quadro de dados
    conn.close()
    return produtos

# Função para realizar uma venda
def realizar_venda(id_produto, quantidade):
    conn = sqlite3.connect("sistema_vendas.db")
    cursor = conn.cursor()

    # Verificar se o produto existe e tem estoque suficiente
    cursor.execute("SELECT estoque FROM produtos WHERE id = ?", (id_produto,))
    estoque = cursor.fetchone()# recupera a próxima linha de um conjunto de resultados de consulta e retorna uma única sequência
    
    #Se não existir produto
    if estoque is None:
        conn.close()
        return "Produto não encontrado"
    estoque = estoque[0]

    #Estoque comm pouca quantidade
    if quantidade > estoque:
        conn.close()
        return "Estoque insuficiente"
    
    # Atualizar o estoque do produto
    novo_estoque = estoque - quantidade
    cursor.execute("UPDATE produtos SET estoque = ? WHERE id = ?", (novo_estoque, id_produto))
    conn.commit()#confirma a modificação da tabela
    conn.close()
    return "Venda realizada com sucesso"


