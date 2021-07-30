"""
32. Faça um programa que calcule o fatorial de um número inteiro fornecido
    pelo usuário.
"""

import math

numero = int(input("\nDigite o número que deseja realizar a fatorial: "))
count = numero
fatorial = math.factorial(numero)

for i in range(numero - 1):
    print(count, end=" * ")
    count -= 1

print("1 = ", fatorial)
