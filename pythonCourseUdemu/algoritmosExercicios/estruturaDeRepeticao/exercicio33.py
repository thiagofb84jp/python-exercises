"""
33. O Departamento Estadual de Meteorologia lhe contratou para desenvolver
    um programa que leia as um conjunto indeterminado de temperaturas, e
    informe ao final a menor e a maior temperaturas informadas, bem como a
    média das temperaturas.
"""

numeroTemperaturas = int(input("Quantidade de temperaturas que irá digitar: "))
temperaturas = []
numeroTemperatura = 1

for i in range(numeroTemperaturas):
    print("Temperatura nº ", numeroTemperatura)
    temperatura = temperaturas.append(float(input("Digite a temperatura: ")))
    numeroTemperatura += 1

print("Maior temperatura: ", max(temperaturas))
print("Menor temperatura: ", min(temperaturas))
print("Média das temperaturas: ", round(
    sum(temperaturas) / len(temperaturas), 2))
