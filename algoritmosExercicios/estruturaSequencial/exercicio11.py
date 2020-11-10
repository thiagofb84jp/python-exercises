"""
1. Faça um Programa que peça 2 números inteiros e um
    número real. Calcule e mostre:
        a) o produto do dobro do primeiro com metade do segundo.
        b) a soma do triplo do primeiro com o terceiro.
        c) o terceiro elevado ao cubo.
"""

n1 = 1
n2 = 2
n3 = 3.2

produto = (2 * n1) * (n2 / 2)
soma = (3 * n1) + n3
cubo = n3**3

print('Produto = {:.2f}'.format(produto))
print('Soma = {:.2f}'.format(soma))
print('Cubo = {:.2f}'.format(cubo))
