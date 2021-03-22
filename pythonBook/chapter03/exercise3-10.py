"""
3.10. Calcular aumento salarial.
"""

salario = float(input("Digite o salário atual: "))
percAumento = float(input("Digite o percentual de aumento: "))

aumento = salario * percAumento / 100

novoSalario = salario + aumento

print(f"Um aumento de {percAumento} % em um salário de R$ {salario}")
print(f"é igual a um aumento de R$ {aumento}")
print(f"Resultando em um novo salário de R$ {novoSalario}")
