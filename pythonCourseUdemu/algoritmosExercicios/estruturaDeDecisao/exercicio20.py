'''
20. Faça um Programa para leitura de três notas parciais
     de um aluno. O programa deve calcular a média alcançada por
      aluno e presentar:
'''

nota1 = 10
nota2 = 9.9
nota3 = 9.5

media = (nota1 + nota2 + nota3) // 3

if (media == 10):
    print("Aprovado com Distinção.")
elif ((media >= 7) and (media < 10)):
    print("Aprovado.")
else:
    print("Reprovado.")
