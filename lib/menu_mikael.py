import funcoes


def menu_principal():
    print("Sistema de Vendas")
    funcoes.criar_tabela_produtos() 
    while True:
        print("\nOpções:")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Realizar Venda")
        print("4. Listar Vendas")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            estoque = int(input("Quantidade em estoque: "))
            funcoes.adicionar_produto(nome, preco, estoque)
            print("Produto adicionado com sucesso!")

        elif escolha == "2":
            produtos = funcoes.listar_produtos()
            print("\nLista de Produtos:")
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Preço: R${produto[2]}, Estoque: {produto[3]}")

        elif escolha == "3":
            id_produto = int(input("ID do produto a ser vendido: "))
            quantidade = int(input("Quantidade a ser vendida: "))
            resultado = funcoes.realizar_venda(id_produto, quantidade)
            print(resultado)

        elif escolha == "4":
            print("em breve...")

        elif escolha == "5":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
