"""
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

a = 30
b = 20
c = 10

if a > c:
    a, c = c, a

if a > b:
    a, b = b, a

if b > c:
    b, c = c, b

print('A ordem decrescente é: {}, {} e {}'.format(a, b, c))
