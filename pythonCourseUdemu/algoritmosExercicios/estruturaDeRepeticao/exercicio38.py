"""
38. Um funcionário de uma empresa recebe aumento salarial anualmente:
    Sabe-se que:
"""

salario = float(input("Digite o salário inicial do funcionário: "))
aumento = 1.5

for i in range(1996, 2018 + 1):
    aumento = aumento * 2
    salarioAtual = salario + (salario * (aumento / 100))
    print("Salário em", i, " = {:.0f}".format(salarioAtual))
