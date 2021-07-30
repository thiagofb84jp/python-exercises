# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input("Valor por hora: "))
horasTrabalhadasMes = float(input("Horas trabalhadas no mês: "))

salario = valorHora * horasTrabalhadasMes

print("Salário: R$ {:.2f}".format(salario))
