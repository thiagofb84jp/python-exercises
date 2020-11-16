"""
5. Faça um programa para a leitura de duas notas parciais de um aluno.
    O programa deve calcular a média alcançada por aluno e apresentar
        uma mensagem.
"""

nota1 = 5
nota2 = 4.5

media = (nota1 + nota2) // 2

if media == 10:
    print("Aprovado com Distinção")
elif (media >= 7) and (media <= 9):
    print("Aprovado")
else:
    print("Reprovado")
