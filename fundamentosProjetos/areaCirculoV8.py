# Criando uma função sem retorno
from math import pi


# Função sem retorno
def circulo(raio):
    print("Área do círculo: {:.2f}".format(pi * float(raio) ** 2))


if (__name__ == '__main__'):
    raio = input("Informe o raio: ")
    circulo(raio)
