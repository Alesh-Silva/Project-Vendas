import sqlite3

class DatabaseManager:
    def __init__(self):
        try:
            import sqlite3
        except ImportError:
            print("Erro ao importar o módulo sqlite3")

        self.conn = sqlite3.connect('Database/security.db')
        self.c = self.conn.cursor()
        self.conn.commit()

    def adicionar_user(self):
        nomeC = input("Qual o nome do novo funcionário?\n")
        cpf = int(input(f"Qual o cpf do(a) {nomeC}?\n"))
        idade = int(input(f"Quanto anos o(a) {nomeC} tem ?\n"))
        user = input(f"Qual o user do {nomeC}\n")
        senha = (input(f"Qual a senha do {user}: \n"))

        # Inserir o nome e o preço na tabela 'inventory'
        sql = "INSERT INTO login (nomeC, cpf, idade, user, senha) VALUES (?, ?, ?, ?, ?)"
        parameters = (nomeC, cpf, idade, user, senha)
        self.c.execute(sql, parameters)
        self.conn.commit()
        print("\033[93mNovo Funcionário adicionado com Sucesso!!!!!!\033[0m")

    def get_max_id(self):
        result = self.c.execute('SELECT MAX(id) FROM login')

        for i in result:
            id = i[0]
            return id

# Criar uma instância da classe DatabaseManager
db_manager = DatabaseManager()

# Exemplo de chamada da função
db_manager.adicionar_user()
