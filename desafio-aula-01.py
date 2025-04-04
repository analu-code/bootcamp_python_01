# DESAFIO DO DIA: CÁLCULO DE BÔNUS COM ENTRADA DO USUÁRIO

# Escreva um programa em Python que solicita ao usuário para digitar seu nome,
nome = str(input("Olá, digite o seu nome e pressione `ENTER`: "))

# o valor do seu salário mensal 
salario = float(input("Agora digite o seu salário: "))

# e o valor do bônus que recebeu. 
bonus = float(input("Agora digite qual é o multiplicador do seu bônus: "))

# KPI de calculo: 1000 + salario * bonus
kpi = (1000 + salario * bonus)

# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome
# e informando o valor do salário em comparação com o bônus recebido.
print(f"O usuário {nome} possui o bônus de {kpi: .2f}")