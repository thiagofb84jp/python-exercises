"""
7. Faça um programa que leia 5 números e informe o maior número.
"""

lista = []

quantidade = 5

for i in range(0, int(quantidade)):
    lista.append(int(input("Digite o número: ")))

print("O maior número da lista é o: {}".format(max(lista)))
