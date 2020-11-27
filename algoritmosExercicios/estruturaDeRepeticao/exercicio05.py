"""
5. Altere o programa anterior permitindo ao usuário informar as
   populações e as taxas de crescimento iniciais. Valide a entrada
   e permita repetir a operação.
"""

populacaoA = int(input("Informe a população da cidade A: "))
populacaoB = int(input("Informe a população da cidade B: "))
ano = 0

taxaCrescimentoA = float(
    input("Informe a taxa de crescimento da população da cidade A: "))
taxaCrescimentoB = float(
    input("Informe a taxa de crescimento da população da cidade B: "))

while (populacaoA <= populacaoB):
    populacaoA += (populacaoA * taxaCrescimentoA) // 100
    populacaoB += (populacaoB * taxaCrescimentoB) // 100
    ano += 1

print("População 'A' possui {} habitantes.".format(populacaoA))
print("População 'B' possui {} habitantes.".format(populacaoB))
print("População 'A' ultrapassará ou igualará a 'B' em {} anos.".format(ano))
