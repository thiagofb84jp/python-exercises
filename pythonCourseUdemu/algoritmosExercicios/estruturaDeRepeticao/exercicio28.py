"""
28. Faça um programa que calcule o valor total investido
    por um colecionador em sua coleção de CDs e o valor médio gasto
    em cada um deles.
"""

quantidadeCDs = int(input("Digite a quantidade de CDs de sua coleção: "))
cds = []
numeroCD = 1

for i in range(quantidadeCDs):
    print("CD número ", numeroCD)
    valorCD = cds.append(float(input("Digite o valor do CD: ")))
    numeroCD += 1

media = sum(cds) / len(cds)
print("A média para cada CD é: {:.2f}".format(media))
