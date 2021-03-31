"""
6.24. Lendo e imprimindo uma lista de compras
"""

# Imprimindo uma lista de compras
compras = ["Maçã", "Laranja", "Limão", "Uva", "Mamão", "Jaca", "Pêra"]

"""
while True:
    produto = input("Produto (digite 'fim' para encerrar): ")
    if produto == "fim":
        break
    compras.append(produto)
"""

print("***** Lista de compras *****")
for x, p in enumerate(compras):
    print(f"[{x + 1}] {p}")


# Impressão de uma lista de strings, letra a letra
L = ["maçãs", "peras", "kiwis"]

for s in L:
    print("")
    for letra in s:
        print(letra)
print("")

# Listas com elementos
produto1 = ["Maçã", 10, 0.30]
produto2 = ["Pêra", 5, 0.75]
produto3 = ["Kiwi", 4, 0.98]

compras = [produto1, produto2, produto3]
for e in compras:
    print(f"Produto: {e[0]}")
    print(f"Quantidade: {e[1]}")
    print(f"Preço: {e[2]:5.2f}")
    print("")
