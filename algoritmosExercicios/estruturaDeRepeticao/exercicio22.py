"""
22. Altere o programa de cálculo dos números primos,
    informando, caso o número não seja primo, por quais
    número ele é divisível.
"""

numero = int(input("Digite um número: "))
lista = []

if ((numero % 2) != 0) or (numero == 2):
    print("É um número primo.")
else:
    for i in range(numero):
        if (numero % (i + 1) == 0):
            lista.append(i + 1)

print("Os números divisíveis por ", numero, "são ", lista)
