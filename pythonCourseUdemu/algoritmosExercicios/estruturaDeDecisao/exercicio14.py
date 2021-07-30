"""
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa
      disciplina ao longo de um semestre, e calcule a sua média.
"""

nota1 = 9.9
nota2 = 9.8

media = (nota1 + nota2) / 2

if (media >= 9.0) and (media <= 10):
    conceito = 'A'
elif (media >= 7.5) and (media < 9.0):
    conceito = 'B'
elif (media >= 6.0) and (media < 7.5):
    conceito = 'C'
elif (media >= 4.0) and (media < 6.0):
    conceito = 'D'
else:
    conceito = 'E'

if (conceito == 'A') or (conceito == 'B') or (conceito == 'C'):
    status = 'APROVADO'
else:
    status = 'REPROVADO'

print("Notas do aluno: {} e {}".format(nota1, nota2))
print("Média: {:.1f}".format(media))
print("Conceito: {}".format(conceito))
print("Caro aluno, você foi {}".format(status))
