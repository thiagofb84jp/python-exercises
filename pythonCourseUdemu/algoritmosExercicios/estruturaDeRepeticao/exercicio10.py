"""
10. Faça um programa que receba dois números inteiros e gere os números
    inteiros que estão no intervalo compreendido por eles.
"""

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

for i in range(numero1 + 1, numero2):
    print(i)
