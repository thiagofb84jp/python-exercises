# For - Parte 3

produto = {'nome': 'Caneta Chic', 'preco': 14.99,
           'importada': True, 'estoque': 793}

# Percorre chaves
for chave in produto:
    print(chave)

print()

# Percorre os valores
for valor in produto.values():
    print(valor)

print()

# Percorre chave/valor
for chave, valor in produto.items():
    print(chave, '=', valor)
