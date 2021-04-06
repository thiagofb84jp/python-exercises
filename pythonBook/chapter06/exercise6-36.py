"""
6.36. Trabalhando com conjuntos (parte II)
"""

ANTES = [1, 2, 5, 6, 9]
DEPOIS = [1, 2, 8, 10]

conjuntoAntes = set(ANTES)
conjuntoDepois = set(DEPOIS)

print("Antes: ", ANTES)
print("Depois: ", DEPOIS, "\n")

print("Elementos que não mudaram :", conjuntoAntes & conjuntoDepois)
print("Elementos novos: ", conjuntoDepois - conjuntoAntes)
print("Elementos que foram removidos: ", conjuntoAntes - conjuntoDepois)
