import os
import datetime
import time

menu_vendas = ["Abrir Caixa", "Sair"]
menu_abrir_caixa = ["Nova Venda","Novo Orçamento", "Encerrar Caixa"]
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

        nova_tela("MENU VENDEDOR")
        data_hora = datetime.datetime.now()
        data_hora_str = data_hora.strftime("%d/%m/%Y %H:%M")
        print(f"CAIXA ABERTO {data_hora_str}")
        
        return True
    


#################################################################
#                         PRINCIPAL
#################################################################


nova_tela("MENU VENDEDOR")
opcao = imprime_opcoes(menu_vendas)


#Menu principal
if opcao == 1:
    nova_tela("MENU VENDEDOR")
    abrir_caixa()

    #Painel do vendedor (Vendas, orçamentos, encerrar caixa e sair)
    opcao_2 = imprime_opcoes(menu_abrir_caixa)
    
    #Nova venda
    if opcao_2 == 1:
        print("Nova Venda")
    
    #Novo Orçamento
    elif opcao_2 == 2:
        print("Novo Orçamento")

    #Encerrar caixa 
    elif opcao_2 == 4:
        print("Encerrar caixa")



elif opcao == 2:
    print("Obrigado por utilizar o Gerentia")
