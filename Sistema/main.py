from vendas import executar_vendas
from listar_dados import buscar_produto
from adicionar_prod import DatabaseManager
import datetime
import intro
import sqlite3


def cabecalho():
    data_hora = datetime.datetime.now()
    data_hora_str = data_hora.strftime("%d/%m/%Y %H:%M")
    print("----- Sistema de Vendas -----")
    print(f"Data e Hora Atuais: {data_hora_str}")
    print("1. Realizar Venda")
    print("2. Lista produtos cadastrados")
    print("3. Cadastrar Produto")
    print("4. Sair")


def main():
    # Conectar ao banco de dados ou criar um novo arquivo de banco de dados se ele não existir
    conn = sqlite3.connect('Database/store.db')

    while True:
        cabecalho()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            executar_vendas()  # Chama a função de vendas
        elif opcao == '2':
            nome_produto = input("Digite o nome do produto que deseja pesquisar (pressione Enter para mostrar todos): ")
            buscar_produto(conn, nome_produto)  # Passa a conexão como argumento
        elif opcao == '3':
            db_manager = DatabaseManager()  # Armazena a instância da classe em uma variável
            db_manager.create_product()  #
        elif opcao == '4':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # Fechar a conexão com o banco de dados
    conn.close()

if __name__ == "__main__":
    main()
