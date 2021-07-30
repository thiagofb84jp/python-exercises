"""
27. Faça um programa que calcule o número médio de
    alunos por turma. Para isto, peça a quantidade de turmas e
    a quantidade de alunos para cada turma.
"""

turmas = int(input("Quantas turmas são registradas? "))

alunosTurmas = []
turma = 1

for i in range(turmas):
    print("Turma ", turma)
    alunos = int(input("Alunos da turma: "))
    while (alunos > 40):
        print("Turma ", turma,
              " [uma turma só pode ter 40 (quarenta) alunos.]")
        alunos = int(input("Alunos da turma: "))
    turma += 1
    alunosTurmas.append(alunos)

media = sum(alunosTurmas) / len(alunosTurmas)
print("A média é igual a: {:.0f}".format(media))
