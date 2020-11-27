# While - Parte 1

# while True:
# print("Vai demorar muuuuuuuuuuuuuito!")

from random import randint

numeroInformado = -1
numeroSecreto = randint(0, 9)

while (numeroInformado != numeroSecreto):
    numeroInformado = int(input("Informe o número: "))

print("Número secreto {} foi encontrado".format(numeroSecreto))
