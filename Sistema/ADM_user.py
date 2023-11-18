import sqlite3
import pwinput

class DatabaseManager:
    def __init__(self):
        try:
            import sqlite3
        except ImportError:
            print("Erro ao importar o módulo sqlite3")

        self.conn = sqlite3.connect('Database/security.db')
        self.c = self.conn.cursor()
        self.conn.commit()

    def listar_usuarios(self):
        result = self.c.execute('SELECT * FROM login')
        
        # Iterar sobre os resultados e imprimir
        for row in result:
            print(row)

    def modificar_usuario_interativo(self):
        try:
            self.listar_usuarios()  # Lista os usuários para que o usuário escolha o ID a ser modificado
            user_id = int(input("Digite o ID do usuário que deseja modificar (ou 0 para cancelar): "))

            if user_id == 0:
                print("Operação cancelada.")
                return

            self.c.execute('SELECT * FROM login WHERE id=?', (user_id,))
            usuario = self.c.fetchone()

            if usuario:
                print(f"\nDetalhes do usuário com ID {user_id}: {usuario}")
                escolha = input("\nDeseja realmente modificar este usuário? (s/n): ").lower()

                if escolha == 's':
                    novo_user = input("Digite o novo nome: ")
                    nova_senha = pwinput.pwinput("Digite a nova senha: ")
                    novo_cargo = input(f"Digite o novo cargo do {novo_user}:\n\033[93mADM\033[0m para administrador ou \033[93mFUNC\033[0m para funcionário:\n").upper()
                    while  novo_cargo != "ADM" and novo_cargo != "FUNC":
                        print("Atenção cargo invalido")
                        cargo = input(f"Digite o cargo do {novo_user}:\n\033[93mADM\033[0m para administrador ou \033[93mFUNC\033[0m para funcionário:\n").upper()

                    # Executar a instrução SQL UPDATE
                    self.c.execute('UPDATE login SET user=?, senha=?, cargo=? WHERE id=?', (novo_user, nova_senha,novo_cargo ,user_id))
                    self.conn.commit()
                    print(f"\033[93mUsuário com ID {user_id} modificado com sucesso.\033[0m")
                else:
                    print("Operação cancelada.")
            else:
                print(f"\033[91mUsuário com ID {user_id} não encontrado.\033[0m")

        except Exception as e:
            print(f"\033[91mErro ao modificar usuário: {e}\033[0m")

# Criar uma instância da classe DatabaseManager
db_manager = DatabaseManager()

# Exemplo de chamada da função para modificar um usuário de forma interativa
db_manager.modificar_usuario_interativo()

# Exemplo de chamada da função para listar usuários após a modificação
db_manager.listar_usuarios()
