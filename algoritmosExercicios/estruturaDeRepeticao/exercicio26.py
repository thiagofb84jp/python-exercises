"""
26. Numa eleição existem três candidatos. Faça um programa que
    peça o número total de eleitores.
"""

eleitores = int(input("Digite o número total de eleitores: "))

candidatoA = 0
candidatoB = 0
candidatoC = 0
votantes = 0

while (votantes < eleitores):
    voto = int(input(
        "Digite 1 para votar no candidato A, 2 para o cancidato B e 3 para o candidato C: "))
    if (voto == 1):
        candidatoA += 1
    elif (voto == 2):
        candidatoB += 1
    elif(voto == 3):
        candidatoC += 1
    votantes += 1

print("O candidato A teve ", candidatoA, "votos.")
print("O candidato B teve ", candidatoB, "votos.")
print("O candidato C teve ", candidatoC, "votos.")
