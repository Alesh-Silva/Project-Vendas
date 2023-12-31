'''antigo main - agora é menur vendedor'''
from vendas import executar_vendas
from listar_dados import buscar_produto
from venda_avulsa import executar_vendas_avulsas
from adicionar_prod import *
from ADM_user import *
from adicionar_user import *
from modificar_produto import *

import datetime
import platform
import os
import sqlite3

def limpar_tela():
    os.system('clear' if platform.system() == 'Linux' else 'cls')
   

def cabecalho():
    
    data_hora = datetime.datetime.now()
    data_hora_str = data_hora.strftime("\033[1;33m%d/%m/%Y %H:%M\033[m")
    print("----- Sistema de Vendas -----")
    print(f"Data e Hora Atuais: {data_hora_str}")
    print("1. Realizar Venda")
    print("2. Realizar Venda Avulsa")
    print("3. Lista produtos cadastrados")
    print("4. Cadastrar Produto")
    print("5. Modificar Produto")
    print("6. Listar Funcionários e Modifcar User")
    print("7. Cadastrar Novo Funcionário")
    print("8. Sair")


def main_adm():
    conn = sqlite3.connect('Database/store.db')   

    while True:
        cabecalho()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            executar_vendas()  # Chama a função de vendas
            time.sleep(5)
            limpar_tela()
        elif opcao == '2':
            executar_vendas_avulsas()
            time.sleep(5)
            limpar_tela()
        elif opcao == '3':
            nome_produto = input("Digite o nome do produto que deseja pesquisar (pressione Enter para mostrar todos): ")
            buscar_produto(conn, nome_produto)  # Passa a conexão como argumento
        elif opcao == '4':
            db_manager = DatabaseManager()  # Armazena a instância da classe em uma variável
            db_manager.create_product()  #
            time.sleep(5)
            limpar_tela()
            
        elif opcao == '5':
            modificador.modificar_produto_interativo()
            time.sleep(5)
            limpar_tela()
            
        elif opcao == '6':
            #db_manager_adm.listar_usuarios() # Lista todos os dados dos funcionários cadastradados
            db_manager_adm.modificar_usuario_interativo()
            time.sleep(5)
            limpar_tela()                
           
        elif opcao == '7':
            db_manager_user.adicionar_user()
            time.sleep(5)
            limpar_tela()
        elif opcao == '8':
            print("Saindo do sistema. Até mais!")
            time.sleep(3)
            from login import Login
            login_obj = Login()
            login_obj.verificacao()
            break  # Sai do loop principal quando o usuário sai do sistema
         
        else:
            print("Opção inválida. Tente novamente.")
            volta = input("Digite quallquer tecla para voltar")

    # Fechar a conexão com o banco de dados
    conn.close()
#main_adm()