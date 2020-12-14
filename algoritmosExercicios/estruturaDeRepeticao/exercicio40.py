"""
40. Foi feita uma estatística em cinco cidades brasileiras
    para coletar dados sobre acidentes de trânsito. Foram obtidos
    os seguintes dados:
"""

codCidades = []
numVeiculos = []
numAcidentes = []
acidentes2000 = []

for i in range(5):
    print("\nCidade número ", i + 1)
    codigoCidade = int(input("Digite o código da cidade: "))
    while (codigoCidade in codCidades):
        print("[Código já digitado!]")
        codigoCidade = int(input("Digite outro código: "))

    numeroAcidentes = int(input("Digite o número de acidentes: "))
    numeroVeiculos = int(input("Digite o número de veículos: "))

    if (numeroVeiculos > 2000):
        acidentes2000.append(numeroAcidentes)
        numAcidentes.append(numeroAcidentes)
    else:
        numAcidentes.append(numeroAcidentes)

    numVeiculos.append(numeroVeiculos)
    codCidades.append(codigoCidade)

indiceAcidentesMenor = numAcidentes.index(min(numAcidentes))
indiceAcidentesMaior = numAcidentes.index(max(numAcidentes))

print("\nMenos acidentes\nQuantidade de acidentes: ", min(numAcidentes),
      "\nCódigo da cidade: ", codCidades[indiceAcidentesMenor])
print("\nMais acidentes\nQuantidade de acidentes: ", max(numAcidentes),
      "\nCódigo da cidade: ", codCidades[indiceAcidentesMaior])

mediaVeiculos = sum(numVeiculos) / len(numVeiculos)
print("\nMédia de veículos nas 5 cidades: ", mediaVeiculos)

mediaAcidentes2000 = sum(acidentes2000) / len(acidentes2000)
print("\nMédia de acidentes nas cidades com menos de 2000 veículos: ",
      mediaAcidentes2000)
