import sqlite3

class Venda:
    def __init__(self, conn, c):
        self.conn = conn
        self.c = c
 
    def realizar_venda(self, produto_id_nome, quantidade_venda):
        # Verificar se há estoque suficiente
        self.c.execute("SELECT id, name, estoque, precoV FROM inventory WHERE id=? OR name=?", (produto_id_nome, produto_id_nome))
        result = self.c.fetchall()

        if result:
            if len(result) == 1:
                # Se houver apenas um resultado, prosseguir normalmente
                product_id, name, estoque_disponivel, preco_venda_unitario = result[0]
                self.realizar_venda_individual(product_id, name, estoque_disponivel, preco_venda_unitario, quantidade_venda)
            else:
                # Se houver mais de um resultado, mostrar as opções ao usuário
                print("Existem múltiplos produtos com o mesmo nome. Escolha o produto pelo ID:")
                for product_id, name, estoque, precoV in result:
                    print(f"ID: {product_id}, Nome: {name}, Estoque: {estoque}, Preço: {precoV}")

                valid_id = False
                while not valid_id:
                    chosen_id = int(input("Digite o ID do produto desejado: "))
                    # Verificar se o ID escolhido está na lista
                    if chosen_id in [item[0] for item in result]:
                        product_id, name, estoque_disponivel, preco_venda_unitario = next(item for item in result if item[0] == chosen_id)
                        self.realizar_venda_individual(product_id, name, estoque_disponivel, preco_venda_unitario, quantidade_venda)
                        valid_id = True  # Sai do loop se o ID for válido
                    else:
                        print("\033[91mID inválido. Tente novamente.\033[0m")
        else:
            print(f"\033[91mProduto com ID ou Nome {produto_id_nome} não encontrado.\033[0m")

    def realizar_venda_individual(self, product_id, name, estoque_disponivel, preco_venda_unitario, quantidade_venda):
        if estoque_disponivel is not None and estoque_disponivel >= quantidade_venda:
            # Calcular o preço total da venda
            preco_total = quantidade_venda * preco_venda_unitario

            print(f"Produto ID: {product_id}, Nome: {name}, Estoque disponível: {estoque_disponivel}, Quantidade vendida: {quantidade_venda}, Preço total: {preco_total}")

            # Perguntar pelo método de pagamento
            metodo_pagamento = input("Digite o método de pagamento (Dinheiro, Cartão, etc.): ").strip().lower()

            # Calcular o troco se o pagamento for em dinheiro
            if metodo_pagamento == 'dinheiro':
                valor_pago = float(input("Digite o valor pago: "))
                troco = valor_pago - preco_total
                if troco < 0:
                    print("\033[91mPagamento insuficiente. Venda não realizada.\033[0m")
                    return
                else:
                    print(f"\033[92mVenda realizada com sucesso!\033[0m")
                    print(f"Pagamento: {metodo_pagamento}, Troco: {troco}")
            elif metodo_pagamento == 'cartao':
                cart = int(input("Digite a quantidade de pacelas, com no máximo 10\n"))
                if cart > 10:
                    print("\033[91mNúmero de parcelas inválido. Venda não realizada.\033[0m")
                    return
                if cart == 1:
                    valor_pago = 1.0 * preco_total
                # se a quantidade de pacelas for 1 o cliente não paragar juros 
                elif cart <= 3:
                    valor_pago = 1.2 * preco_total 
                 # se a quantidade de pacelas for <=3 o cliente pagarar 20 % a mais no valor do produto
                else:
                    valor_pago =  1.3 * preco_total
                # se a quantidade de pacelas for >= 3 o cliente pagarar 30 % a mais no valor do produto
                print(f"\033[92mVenda realizada com sucesso!\033[0m")
                print(f"Pagamento: {metodo_pagamento}, Valor total: {valor_pago}")
            else:
                print(f"\033[92mVenda realizada com sucesso!\033[0m")
                print(f"Pagamento: {metodo_pagamento}")
                
            # Atualizar o estoque
            novo_estoque = estoque_disponivel - quantidade_venda
            self.c.execute("UPDATE inventory SET estoque=? WHERE id=?", (novo_estoque, product_id))
            self.conn.commit()

            # Verificar se o estoque é zero e excluir o produto se for o caso
            if novo_estoque == 0:
                self.c.execute("DELETE FROM inventory WHERE id=?", (product_id,))
                self.conn.commit()
        else:
            print("\033[91mEstoque insuficiente para realizar a venda.\033[0m")

# Conectar ao banco de dados ou criar um novo arquivo de banco de dados se ele não existir
conn = sqlite3.connect('Database/store.db')
c = conn.cursor()

# Criar uma instância da classe Venda
venda = Venda(conn, c)

# Exemplo de uso
produto_id_nome = input("Digite o ID ou o Nome do produto que deseja vender:\n")
quantidade_venda = float(input(f"Digite a quantidade de {produto_id_nome} que deseja vender:\n"))

# Realizar a venda
venda.realizar_venda(produto_id_nome, quantidade_venda)

# Fechar a conexão com o banco de dados
conn.close()
