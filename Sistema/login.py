import sqlite3
import pwinput
from menur_vendedor import main
import time
import os
import platform
def limpar_tela():
    os.system('clear' if platform.system() == 'Linux' else 'cls')    
class Login:
    def __init__(self):
        try:
            import sqlite3
        except ImportError:
            print("Erro ao importar o módulo sqlite3")

        self.conn = sqlite3.connect('Database/security.db')
        self.c = self.conn.cursor()
        

    def verificacao(self):
        limpar_tela()
        user = input("User:")
        senha = pwinput.pwinput("Senha:")

        if user and senha:
            # Use uma consulta parametrizada para evitar SQL injection
            self.c.execute("SELECT * FROM login WHERE user=? AND senha=?", (user, senha))
            resultado = self.c.fetchone()

            if resultado:
                print("Login bem-sucedido!")
                 # Verifique o cargo do usuário logado
                self.c.execute("SELECT cargo FROM login WHERE user=?", (user,))
                resultado_cargo = self.c.fetchone()

                if resultado_cargo:
                    cargo = resultado_cargo[0]

                    if cargo == 'ADM':
                        print("O usuário tem cargo de administrador.")
                        # Exibir mensagem específica para ADM
                        print("Bem-vindo ao sistema de administrador!")
                    elif cargo == 'FUNC':
                        print(f"O {user} tem cargo de funcionário.")   #o user só está aqui para quando o user fizer login, vai abrir o sistema com base em seu cargo                     
                        time.sleep(3)
                        limpar_tela()
                        main()
                        # Abrir o main que está na pasta Sistema
                        # Substitua o comando abaixo pelo que você precisa para abrir o main
                        # Exemplo: subprocess.Popen(["python", "caminho/do/main.py"])
                    else:
                        print("Cargo desconhecido.")
                else:
                    print("Cargo não encontrado para o usuário.")

            else:
                print("Usuário ou senha incorretos.")
        else:
            print("Usuário ou senha não fornecidos.")

        self.conn.commit()

# Exemplo de uso
if __name__ == "__main__":
    login_obj = Login()
    login_obj.verificacao()
