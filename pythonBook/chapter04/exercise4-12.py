"""
4.12. Calcula salário trabalhador
"""

salario = float(input("Digite o valor do salário: "))

if (salario <= 1250):
    aumento = salario + (salario * 0.15)
    novoSalario = salario + aumento
