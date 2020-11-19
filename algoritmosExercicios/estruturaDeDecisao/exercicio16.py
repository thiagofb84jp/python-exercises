"""
16. Faça um programa que calcule as raízes de uma equação do segundo grau,
       na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c
        e fazer as consistências, informando ao usuário
            nas seguintes situações:
"""
import math

a = 1
b = 6
c = 7

if (a == 0):
    print("Não é uma equação do 2º grau.")
else:
    delta = b ** b - (4 * a * c)

    if (delta < 0):
        print("Delta menor que zero. Raízes imaginárias.")
    elif (delta == 0):
        raiz = -b / (2 * a)
        print("Delta = {:.0f}, Raiz = {:.0f}".format(delta, raiz))
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Raízes = {:.0f} e {:.0f}".format(raiz1, raiz2))
