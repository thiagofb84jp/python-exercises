# Um pouco sobre o módulo
from math import pi

raio = input("Informe o raio: ")
print("Área do círculo: {:.2f}".format(pi * float(raio) ** 2))

print("Nome do módulo: ", __name__)
print("Nome do pacote: ", __package__)
