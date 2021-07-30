'''
47. Em uma competição de ginástica, cada atleta
    recebe votos de sete jurados. A melhor e a pior
    nota são eliminadas. A sua nota fica sendo a média
    dos votos restantes.
'''

import time

nomeAtleta = True
numeroAtleta = 1

while (nomeAtleta != ''):
    notas = []
    print("\n" * 5)
    print("Atleta nº ", numeroAtleta)
    nomeAtleta = input("Digite o nome do atleta: ")
    if (nomeAtleta == ''):
        break
    else:
        numeroJurado = 1
        print("\n" * 3)
        for i in range(7):
            print("Jurado nº ", numeroJurado)
            nota = float(input("Digite a nota: "))
            while ((nota < 0) or (nota > 10)):
                print("[Nota inválida!]")
                nota = float(
                    input("Por favor, digite a nota [entre 0 e 10]: "))
            notas.append(nota)
            numeroJurado += 1
        print("Atleta: ", nomeAtleta)
        numeroJurado = 1
        count = 0
        for i in range(7):
            print(numeroJurado, "° Jurado: ", notas[count])
            numeroJurado += 1
            count += 1

        print("Resultado Final: ")
        print("Nome do atleta: ", nomeAtleta)
        print("Melhor nota: ", max(notas))
        print("Pior nota: ", min(notas))
        notas.remove(max(notas))
        notas.remove(min(notas))
        media = sum(notas) / len(notas)
        print("Média: ", round(media, 2))

        numeroAtleta += 1

        print("Reiniciando em 5 segundos...")
        time.sleep(5)
