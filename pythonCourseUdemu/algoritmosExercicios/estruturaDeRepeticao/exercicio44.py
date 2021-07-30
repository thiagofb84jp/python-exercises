"""
44. Em uma eleição presidencial existem quatro candidatos.
    Os votos são informados por meio de código.
"""

possiveisVotos = [1, 2, 3, 4, 5, 6]
candidatos = ['Ciro Gomes', 'Jair Bolsonaro',
              'João Amoedo', 'Lula Molusco', 'Nulo', 'Branco']
votos = []

voto = True
numeroVotos = 1

while (voto != 0):
    print("Voto nº ", numeroVotos)
    voto = int(input("Digite o seu voto: "))
    if voto == 0:
        break
    else:
        while (voto not in possiveisVotos):
            print("[Voto inválido.]")
            voto = int(input("Digite o seu voto: "))
        votos.append(voto)
    numeroVotos += 1

contador = 0
print("\n" * 2)

for i in range(len(candidatos)):
    print("Votos para ", candidatos[contador], end=" : ")
    if (votos.count == 0):
        print("0")
        contador += 1
    else:
        print(votos.count(contador + 1))
        contador += 1

porcentagemNulo = (votos.count(5) / len(votos)) * 100
porcentagemBranco = (votos.count(6) / len(votos)) * 100

print("\nPorcentagem Nulos: ", round(porcentagemNulo, 2),
      "%\nPorcentagem Brancos: ", round(porcentagemBranco, 2), "%")
