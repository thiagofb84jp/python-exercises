# Adicionando retorno à função
from math import pi


# Função sem retorno
def circulo(raio):
    return pi * float(raio) ** 2


if (__name__ == '__main__'):
    raio = input("Informe o raio: ")
    area = circulo(raio)
    print("Área do círculo: {:.2f}".format(area))
