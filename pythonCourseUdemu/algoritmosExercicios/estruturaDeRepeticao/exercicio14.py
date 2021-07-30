"""
14. Faça um programa que peça 10 números inteiros,
    calcule e mostre a quantidade de números pares
    e a quantidade de números impares.
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))
n5 = int(input("Digite um número: "))
n6 = int(input("Digite um número: "))
n7 = int(input("Digite um número: "))
n8 = int(input("Digite um número: "))
n9 = int(input("Digite um número: "))
n10 = int(input("Digite um número: "))

listaNumeros = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

pares = 0
impares = 0

for i in listaNumeros:
    if ((i % 2) == 0):
        pares += 1
    else:
        impares += 1

print("Os pares são: {}".format(pares))
print("Os ímpares são: {}".format(impares))
