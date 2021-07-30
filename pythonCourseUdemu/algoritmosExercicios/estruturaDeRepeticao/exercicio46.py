"""
46. Em uma competição de salto em distância cada atleta tem
    direito a cinco saltos. No final da série de saltos de cada
    atleta, o melhor e o pior resultados são eliminados. O seu
    resultado fica sendo a média dos três valores restantes.
"""

nomeAtleta = True
numeroAtleta = 1

while (nomeAtleta != ''):
    saltos = []
    print("\n" * 5)
    print("Atleta nº ", numeroAtleta)
    nomeAtleta = input("Digite o nome do atleta: ")
    if (nomeAtleta == ''):
        break
    else:
        numeroSalto = 1
        print("\n" * 3)
        for i in range(5):
            print("Salto nº", numeroSalto)
            distanciaSalto = float(input("Digite a distância do salto: "))
            saltos.append(distanciaSalto)
            numeroSalto += 1
        print("Atleta: ", nomeAtleta)
        numeroSalto = 1
        count = 0
        for i in range(5):
            print(numeroSalto, "° salto : ", saltos[count], " m")
            numeroSalto += 1
            count += 1
        print("Melhor salto: ", max(saltos), " m")
        print("Pior salto: ", min(saltos), " m")

        saltos.remove(max(saltos))
        saltos.remove(min(saltos))
        media = sum(saltos) / len(saltos)
        print("Média dos demais saltos: ", round(media, 2))
        print("Resultado Final: \n", nomeAtleta, " : ", round(media, 2))
        numeroAtleta += 1
