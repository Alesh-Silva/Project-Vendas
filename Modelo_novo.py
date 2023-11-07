#def menu_principal():
#    print("1. Abrir Caixa")
#    print("2. Fechar Caixa")
#    print("3. Relatórios")
#    print("")

menu_principal = ["Abrir Caixa", "Fechar Caixa", "Relatórios", "Sair", "Teste"]

def imprime_opcoes(lista):
    indice = 0
    for i in lista:
        indice += 1
        print(f"[{indice}] {i}")

    opcao = int(input("Informe a opção desejada:"))
    return opcao


imprime_opcoes(menu_principal)