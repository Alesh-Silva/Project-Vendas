from datetime import datetime

# Obtendo a data e hora atual
data_hora = datetime.now()

# Exemplos de formatação
formato1 = data_hora.strftime("%d/%m/%Y %H:%M:%S")
formato2 = data_hora.strftime("%A, %d %B %Y %I:%M %p")
formato3 = data_hora.strftime("%Y-%m-%d %H:%M:%S")

# Imprimindo os resultados
print("Formato 1:", formato1)
print("Formato 2:", formato2)
print("Formato 3:", formato3)
