"""
11. Altere o programa anterior para mostrar no final a soma dos números.
"""

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

for i in range(numero1 + 1, numero2):
    print(i)

for i in range(numero2 + 1, numero1):
    print(i)

print("Soma dos números: {}".format(i + i))
