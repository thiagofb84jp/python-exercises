"""
39. Faça um programa que leia dez conjuntos de dois valores,
    o primeiro representando o número do aluno e o segundo
    representando a sua altura em centímetros.
"""

numeroAlunos = []
alturaAlunos = []

for i in range(10):
    print("\nDigitação número ", i + 1, " :")
    numeroAluno = int(input("Digite o número do aluno: "))
    while (numeroAluno in numeroAlunos):
        print("[Este número já foi digitado]")
        numeroAluno = int(input("Digite outro número: "))
    alturaAluno = alturaAlunos.append(
        float(input("Digite a altura do aluno: ")))
    numeroAlunos.append(numeroAluno)

indiceBaixo = alturaAlunos.index(min(alturaAlunos))
indiceAlto = alturaAlunos.index(max(alturaAlunos))

print("Aluno mais baixo \nNúmero: ",
      numeroAlunos[indiceBaixo], "\nAltura: ", min(alturaAlunos))
print("Aluno mais alto \nNúmero: ",
      numeroAlunos[indiceAlto], "\nAltura: ", max(alturaAlunos))
