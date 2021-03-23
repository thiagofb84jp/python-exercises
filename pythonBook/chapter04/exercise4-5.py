"""
4.5. Calcula salário trabalhador
"""

salario = float(input("Digite seu salário: "))

if (salario <= 1250):
    aumento = salario * 0.15
    novoSalario = salario + aumento
else:
    aumento = salario * 0.10
    novoSalario = salario + aumento

print(f"O novo aumento é de R${aumento:.2f}")
print(f"Portanto, seu salário será de R${novoSalario:.2f}")
