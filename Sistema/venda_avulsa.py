from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

class Venda:
    def __init__(self):
        self.produtos_venda = []
        self.cart = None

    def adicionar_produto(self, nome, preco, quantidade):
        self.produtos_venda.append((nome, preco, quantidade))

    def criar_nota_fiscal_pdf(self, total_venda, metodo_pagamento):
        # Obter a data e hora atual
        data_hora = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        
        if not os.path.exists("Notas_Fiscais"):
            os.makedirs("Notas_Fiscais")

        # Criar um arquivo PDF
        pdf_path = f"Notas_Fiscais/Nota_Fiscal_{data_hora}.pdf"
        pdf = canvas.Canvas(pdf_path, pagesize=letter)

        # Adicionar informações à nota fiscal
        pdf.setFont('Courier-Bold', 14)
        pdf.drawString(220, 770, "Nota Fiscal")
        pdf.setFont('Courier-Bold', 12)
        pdf.drawString(130, 750, f"Data e Hora: {data_hora} da Compra")

        if metodo_pagamento == 'cartao':
            pdf.drawString(130, 730, f"Valor Total Pago: R${total_venda} em {self.cart} vezes no {metodo_pagamento.upper()}")
        else:
            pdf.drawString(130, 730, f"Valor Total Pago: R${total_venda} no {metodo_pagamento.upper()}")

        y_coord = 700  # Coordenada Y inicial
        for nome, preco, quantidade in self.produtos_venda:
            pdf.setFont('Courier-Bold', 8)
            pdf.drawString(220, y_coord, f"Produto: {nome}")
            pdf.drawString(220, y_coord - 12, f"Quantidade: {quantidade}")
            pdf.drawString(220, y_coord - 24, f"Preço Unitário: R${preco:.2f}")

            if metodo_pagamento == 'cartao':
                pdf.drawString(220, y_coord - 36, f"Valor Total Pago: R${quantidade * preco}")
                pdf.drawString(220, y_coord - 48, f"Método de pagamento {metodo_pagamento.upper()}")
                pdf.drawString(0, y_coord - 53, "...............................................................................................................................................................................")
            else:
                pdf.drawString(220, y_coord - 36 , f"Valor Total Pago: R${quantidade * preco}")
                pdf.drawString(220, y_coord - 48, f"Método de Pagamento: {metodo_pagamento.upper()}")
                pdf.drawString(0, y_coord - 53, "...............................................................................................................................................................................")

            y_coord -= 59  # Diminuir a coordenada Y para o próximo produto
            pdf.drawString(200, 83, f"Código de Barras:")

        # Adicionar imagens ao PDF (conforme seu código original)
        icon = "img/icon_lampada.png"
        pdf.drawInlineImage(icon, 500, 693, width=100, height=100)
        seguranca = "img/seguranca.png"
        pdf.drawInlineImage(seguranca, 100, 120, width=420, height=210)
        qrcode_path = "img/qrcode-pix.png"
        pdf.drawInlineImage(qrcode_path, 510, 10, width=100, height=100)
        qrcodeo2_path = "img/codbarras.png"
        pdf.drawInlineImage(qrcodeo2_path, 15, 12, width=480, height=60)

        # Salvar o arquivo PDF
        pdf.save()
        print(f"Verifique sua nota fiscal em ({pdf_path})")

    def realizar_venda(self):
        total_venda = 0

        for nome, preco, quantidade in self.produtos_venda:
            total_venda += preco * quantidade

        print(f"\033[33mTotal da venda: {total_venda}\033[0m")

        if total_venda > 0:
            metodo_pagamento = input("Digite o método de pagamento (Dinheiro, Cartão, etc.): ").strip().lower()

            if metodo_pagamento == 'dinheiro':
                valor_pago = float(input("Digite o valor pago: "))
                troco = valor_pago - total_venda
                if troco < 0:
                    print("\033[91mPagamento insuficiente. Venda não realizada.\033[0m")
                else:
                    print(f"\033[92mVenda realizada com sucesso!\033[0m")
                    print(f"Pagamento: {metodo_pagamento}, Troco: {troco}")
                    self.criar_nota_fiscal_pdf(total_venda, metodo_pagamento)
            elif metodo_pagamento == 'cartao':
                print("Cada \033[93mn\033[0m pacelas, aumenta em \033[93mn\033[0m por cento no valor do produto \n Exemplo: \033[93m10R$ em 10 pacelas é 11\033[0m")
                cart = int(input("Digite a quantidade de pacelas, com no máximo \033[93m[ 10 ]\033[0m\n"))
                self.cart = cart
                if cart > 10:
                    print("\033[91mNúmero de parcelas inválido. Venda não realizada.\033[0m")
                else:
                    valor_pago = total_venda + (total_venda * cart * 0.01)
                    print(f"\033[92mVenda realizada com sucesso!\033[0m")
                    print(f"Pagamento: {metodo_pagamento}, Valor total: {valor_pago}")
                    self.criar_nota_fiscal_pdf(total_venda, metodo_pagamento)
            else:
                print(f"\033[92mVenda realizada com sucesso!\033[0m")
                print(f"Pagamento: {metodo_pagamento}")
                self.criar_nota_fiscal_pdf(total_venda, metodo_pagamento)

# Função para executar as vendas
def executar_vendas_avulsas():
    venda = Venda()

    while True:
        nome_produto = input("Digite o nome do produto que deseja vender (ou 'não' para encerrar):\n")

        if nome_produto.lower() == 'não':
            break

        preco_produto = float(input(f"Digite o preço unitário de {nome_produto}:\n"))
        quantidade_venda = float(input(f"Digite a quantidade de {nome_produto} que deseja vender:\n"))

        venda.adicionar_produto(nome_produto, preco_produto, quantidade_venda)

    venda.realizar_venda()

# Executar vendas avulsas
#executar_vendas_avulsas()
