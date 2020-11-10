"""
1. Faça um Programa que pergunte quanto você ganha por hora e
    o número de horas trabalhadas no mês.
"""

valorHoraTrabalhada = 35.98
horasTrabalhadas = 220

salarioBruto = valorHoraTrabalhada * horasTrabalhadas
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = impostoRenda + inss + sindicato

salarioLiquido = salarioBruto - descontos

print("Salário Bruto = {:.2f}".format(salarioBruto))
print("Imposto de Renda = {:.2f}".format(impostoRenda))
print("INSS = {:.2f}".format(inss))
print("Sindicato = {:.2f}".format(sindicato))
print("Total dos descontos = {:.2f}".format(descontos))
print("Salário Líquido = {:.2f}".format(salarioLiquido))
