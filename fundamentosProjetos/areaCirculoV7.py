# Testando se é o módulo principal
from math import pi

if (__name__ == '__main__'):
    raio = input("Informe o raio: ")
    print("Área do círculo: {:.2f}".format(pi * float(raio) ** 2))
