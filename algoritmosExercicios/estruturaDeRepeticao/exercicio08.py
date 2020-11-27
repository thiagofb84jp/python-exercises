"""
8. Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

numero1 = float(input("Número 1: "))
numero2 = float(input("Número 2: "))
numero3 = float(input("Número 3: "))
numero4 = float(input("Número 4: "))
numero5 = float(input("Número 5: "))

soma = numero1 + numero2 + numero3 + numero4 + numero5
media = soma / 5

print("Soma total: {}".format(soma))
print("Média total: {}".format(media))
