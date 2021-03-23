"""
4.6. Calcula preço da passagem
"""

distancia = float(input("Digite a distância a percorrer: "))

if distancia <= 200:
    passagem = 0.5 * distancia
else:
    passagem = 0.45 * distancia

print(f"Preço da passagem: R${passagem:7.2f}")
