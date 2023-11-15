import sqlite3

class Login:
    def __init__(self):
        try:
            import sqlite3
        except ImportError:
            print("Erro ao importar o módulo sqlite3")

        self.conn = sqlite3.connect('Database/security.db')
        self.c = self.conn.cursor()

    def verificacao(self):
        user = input("User:")
        senha = input("Senha:")

        if user and senha:
            # Use uma consulta parametrizada para evitar SQL injection
            self.c.execute("SELECT * FROM login WHERE user=? AND senha=?", (user, senha))
            resultado = self.c.fetchone()

            if resultado:
                print("Login bem-sucedido!")
            else:
                print("Usuário ou senha incorretos.")
        else:
            print("Usuário ou senha não fornecidos.")

        self.conn.commit()

# Exemplo de uso
login_obj = Login()
login_obj.verificacao()
