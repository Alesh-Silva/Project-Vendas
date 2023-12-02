import sqlite3
import time

class ProdutoModificador:
    def __init__(self, database_path='Database/store.db'):
        self.conn = sqlite3.connect(database_path)
        self.c = self.conn.cursor()

    def obter_produto_por_identificador(self, produto_identifier):
        try:
            try:
                produto_id = int(produto_identifier)
                self.c.execute('SELECT * FROM inventory WHERE id=?', (produto_id,))
            except ValueError:
                self.c.execute('SELECT * FROM inventory WHERE name=?', (produto_identifier,))

            return self.c.fetchone()
        except Exception as e:
            raise Exception(f"Erro ao obter produto por identificador: {e}")

    def imprimir_detalhes_produto(self, produto):
        print(f"\nDetalhes do produto: {produto}")

    def confirmar_modificacao(self):
        escolha = input("\nDeseja realmente modificar este produto? (s/n): ").lower()
        while escolha != "s" and escolha != 'n':
            print("Digite uma opção válida")
            time.sleep(2)
            escolha = input("\nDeseja realmente modificar este produto? (s/n): ").lower()

        return escolha == 's'

    def modificar_produto(self, produto_id, novo_nome, novo_preco, novo_estoque):
        try:
            self.c.execute('UPDATE inventory SET name=?, precoV=?, estoque=? WHERE id=?',
                           (novo_nome, novo_preco, novo_estoque, produto_id))
            self.conn.commit()
            print("\033[93mProduto modificado com sucesso.\033[0m")
            print("\033[93mAlterações:")
            print(f"  Nome: {novo_nome}")
            print(f"  Preço: {novo_preco}")
            print(f"  Estoque: {novo_estoque}\033[0m")
        except Exception as e:
            raise Exception(f"Erro ao modificar produto: {e}")

    def modificar_produto_interativo(self):
        try:
            produto_identifier = input("Digite o ID ou o nome do produto que deseja modificar (ou 0 para cancelar): ")

            if produto_identifier.lower() == '0':
                print("Operação cancelada.")
                return

            produto = self.obter_produto_por_identificador(produto_identifier)

            if produto:
                self.imprimir_detalhes_produto(produto)

                if self.confirmar_modificacao():
                    novo_nome = input("Digite o novo nome (deixe em branco para manter o valor atual): ").strip()
                    novo_preco = float(input("Digite o novo preço (deixe em branco para manter o valor atual): ") or produto[2])
                    novo_estoque = int(input("Digite o novo estoque (deixe em branco para manter o valor atual): ") or produto[3])

                    self.modificar_produto(produto[0], novo_nome, novo_preco, novo_estoque)
                else:
                    print("Operação cancelada.")
            else:
                print("\033[91mProduto não encontrado.\033[0m")

        except Exception as e:
            print(f"\033[91mErro ao modificar produto: {e}\033[0m")

modificador = ProdutoModificador()


#modificador.modificar_produto_interativo()
