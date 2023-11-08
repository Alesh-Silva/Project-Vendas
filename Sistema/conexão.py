import sqlite3

try:
    import sqlite3
except ImportError:
    print("Erro ao importar o módulo sqlite3")
# Conectar ao banco de dados ou criar um novo arquivo de banco de dados se ele não existir
conn = sqlite3.connect('Database/store.db')
c = conn.cursor()


class DataBase:
    def __init__(self):
        self.name_e = input("Qual o nome do produto?\n")
        self.preco_e = float(input("Qual o valor de compra do produto?\n"))
        self.estoque_e = float((input(f"Quantos {self.name_e} foram comprados ?\n")))
        self.precoV_e = float(input(f"Qual valor de venda do produto {self.name_e}\n"))

    def get_items(self):
        name = self.name_e
        preco = self.preco_e
        precoV = self.precoV_e
        estoque = self.estoque_e
        lucro = (precoV * estoque) - (preco * estoque)

        # Inserir o nome e o preço na tabela 'inventory'
        sql = "INSERT INTO inventory (name, precoC, precoV, estoque,lucro) VALUES (?, ?, ?, ?, ?)"
        parameters = (name, preco, precoV, estoque, lucro)
        c.execute(sql, parameters)
        conn.commit()
        print("Produto inserido com sucesso !!")

def get_max_id():
    result = c.execute('SELECT MAX(id) FROM inventory')

    for i in result:
        id = i[0]
        return id

# Criar uma instância da classe DataBase
db = DataBase()

# Chamar o método get_items para inserir um produto
db.get_items()

# Obter o ID máximo após a inserção
max_id = get_max_id()
print(f"Produto {db.name_e}, foi inserido com ID : {max_id}°")



# Fechar a conexão com o banco de dados
conn.close()