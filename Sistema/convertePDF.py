import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

def gerar_codigo_de_barras_falso(dados):
    # Cada caractere representa uma barra, e o tamanho da barra é sempre 1 (fina)
    codigo_barras = "|"
    for char in dados:
        codigo_barras += "█"  # Use "█" para barras finas
    codigo_barras += "|"
    return codigo_barras

def criar_nota_fiscal(produto, preco, metodo_pagamento):
    # Obter a data e hora atual
    data_hora = datetime.now().strftime("%d-%m-%Y %H:%M")

    # Nome da pasta onde as notas fiscais serão armazenadas
    pasta_notas_fiscais = "Notas_Fiscais"

    # Verificar se a pasta já existe, se não, criar
    if not os.path.exists(pasta_notas_fiscais):
        os.makedirs(pasta_notas_fiscais)

    # Substituir caracteres inválidos no nome do arquivo
    nome_arquivo = f"{pasta_notas_fiscais}/Nota_Fiscal_{data_hora}.pdf"
    nome_arquivo = nome_arquivo.replace("/", "_").replace(":", "-")

    # Criar um arquivo PDF
    pdf = canvas.Canvas(nome_arquivo, pagesize=letter)

    # Adicionar informações à nota fiscal
    pdf.setFont('Helvetica', 12)  # Usando a fonte padrão 'Helvetica'
    pdf.drawString(100, 700, "Nota Fiscal")
    pdf.drawString(100, 680, f"Data e Hora: {data_hora}")
    pdf.drawString(100, 660, f"Produto: {produto}")
    pdf.drawString(100, 640, f"Preço: R${preco:.2f}")
    pdf.drawString(100, 620, f"Método de Pagamento: {metodo_pagamento}")

    # Adicionar o código de barras falso
    codigo_dados = f"{data_hora}{produto}{preco:.2f}{metodo_pagamento}"
    codigo_barras = gerar_codigo_de_barras_falso(codigo_dados)
    pdf.drawString(100, 600, "Código de Barras:")
    pdf.drawString(100, 580, codigo_barras)

    # Salvar o arquivo PDF
    pdf.save()

    print(f"Nota fiscal gerada com sucesso: {nome_arquivo}")

# Exemplo de uso
produto = "Produto A"
preco = 100.0
metodo_pagamento = "Cartão de Crédito"

criar_nota_fiscal(produto, preco, metodo_pagamento)
