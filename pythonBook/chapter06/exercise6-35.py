"""
6.35. Trabalhando com conjuntos (parte I)
"""

L1 = [1, 2, 6, 8]
L2 = [3, 6, 8, 9]

print(f"Lista 1: {L1}")
print(f"Lista 2: {L2}\n")

conjunto1 = set(L1)
conjunto2 = set(L2)

print("Valores comuns às duas listas: ", conjunto1 & conjunto2)
print("Valores que só existem na primeira: ", conjunto1 - conjunto2)
print("Valores que só existem na segunda: ", conjunto2 - conjunto1, "\n")

print("Elementos não repetidos nas duas listas: ", conjunto1 ^ conjunto2, "\n")
print("Primeira lista, sem os elementos repetidos na segunda: ",
      conjunto1 - conjunto2)
