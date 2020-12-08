# Faça um programa que calcule o mostre a média aritmética de N notas.

numeroNotas = int(input("Digite o número de notas que você irá digitar: "))
count = 0
todasNotas = []

while (count < numeroNotas):
    notas = todasNotas.append(float(input("Digite a nota: ")))
    count += 1

media = sum(todasNotas) / numeroNotas
print("A média é igual a: {:.2f}".format(media))
