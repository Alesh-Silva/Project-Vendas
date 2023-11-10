import os
import datetime
import time
from vendas import Venda
# importação do modulo vendas
conn = None
c = None

def importar_vendas():
    return Venda(conn, c) 

menu_vendas = ["Abrir Caixa", "Sair"]
menu_abrir_caixa = ["\033[93mAdicionar um novo produto\033[0m","Novo Orçamento", "Encerrar Caixa","Nova venda"]
menu_fechar_caixa = []
S_N = ["Sim", "Não"]
vendas_dia = []
'''Limpa a tela '''
def limpar_tela():
    os.system("clear" or "cls") # primeiro tenta limpar a tela com system unix depois windows

#imprime cabeçalho com nome do parametro informado
def nova_tela(nome_cabecalho):
    limpar_tela()
    print("="*38)
    print(f"             {nome_cabecalho}")
    print("="*38)

#Recebe uma lista como parametro e imprime em forma de opções com seus respectivos indices iniciando por 1
#Retorna como a variavel opcao o valor referente ao indice informado pelo usuário de acordo com seu interesse
def imprime_opcoes(lista):
    indice = 0
    for i in lista:
        indice += 1
        print(f"[{indice}] {i}")

    opcao = int(input("Informe a opção desejada:"))
    return opcao

#Abre um novo caixa e informa data e hora da abertura
def abrir_caixa():
    print("Deseja abrir um novo caixa?")
    confima_abertura =  imprime_opcoes(S_N)
    
    if confima_abertura == 1:        

        nova_tela("\033[43mMENUR VENDEDOR\033[0m")
        data_hora = datetime.datetime.now()
        data_hora_str = data_hora.strftime("%d/%m/%Y %H:%M")
        print(f"CAIXA ABERTO {data_hora_str}")
        
        return True
    

programa_rodando = True
caixa_aberto = False

while programa_rodando:
    nova_tela("MENU VENDEDOR")
    opcao = imprime_opcoes(menu_vendas)

    if opcao == 1:
        nova_tela("MENU VENDEDOR")

        if not caixa_aberto:
            if abrir_caixa():
                caixa_aberto = True
                print("Caixa aberto com sucesso!")
            else:
                print("Caixa não aberto.")
        else:
            Caixa_aberto = imprime_opcoes(menu_abrir_caixa)

            if Caixa_aberto == 1:
                if caixa_aberto:
                    venda = importar_vendas()
                    product_id = int(input("Digite o ID do produto que deseja vender:\n"))
                    quantidade_venda = float(input("Digite a quantidade que deseja vender:\n"))
                    venda.realizar_venda(product_id, quantidade_venda)
                else:
                    print("O caixa não está aberto. Abra o caixa antes de realizar uma venda.")
            elif Caixa_aberto == 2:
                print("Novo Orçamento")
            elif Caixa_aberto == 3:
                print("Encerrar Caixa")
                caixa_aberto = False
            elif Caixa_aberto == 4:
                print("Nova Venda")
            else:
                print("Obrigado por utilizar o Gerentia")
                programa_rodando = False