"""
45. Desenvolver um programa para verificar a nota do aluno em uma prova
    com 10 questões, o programa deve perguntar ao aluno a resposta de cada
    questão e ao final comparar com o gabarito da prova e assim calcular
    o total de acertos e a nota (atribuir 1 ponto por resposta certa).
"""

gabarito = []
respostasAluno = []
notasTiradas = []
print("\nProfessor: ")

for i in range(10):
    print("Questão: ", i + 1)
    respostaCerta = gabarito.append(input("Digite a alternativa correta: "))

numeroAluno = 1
continuar = True

while (continuar != 'n'):
    print("\n" * 5)
    print("Aluno nº", numeroAluno, ":")
    respostasAluno.clear()
    for i in range(10):
        print("Questão: ", i + 1)
        respostaAluno = respostasAluno.append(input("Escolha a alternativa: "))
    nota = 0
    for i in range(10):
        if (respostasAluno[1] == gabarito[i]):
            nota += 1
    notasTiradas.append(nota)
    continuar = input("Outro aluno vai utilizar o sistema? [s/n]: ")
    numeroAluno += 1

print(len(notasTiradas), " alunos utilizaram o sistema.")
print("\nA maior nota tirada foi: ", max(notasTiradas))
print("A menor nota tirada foi: ", min(notasTiradas))
print("A média de notas da turma foi de: ",
      sum(notasTiradas) / len(notasTiradas))
print(notasTiradas)
