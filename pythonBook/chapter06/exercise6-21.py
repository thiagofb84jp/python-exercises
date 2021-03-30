"""
6.21. Percorrendo listas
"""
# Verificação de maior valor
L = [1, 7, 2, 4, 0, 15]
maximo = L[0]
minimo = L[0]

print("Imprimindo valores máximo e mínimo da lista: ")
for e in L:
    if e > maximo:
        maximo = e
    elif e < minimo:
        minimo = e

print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")
