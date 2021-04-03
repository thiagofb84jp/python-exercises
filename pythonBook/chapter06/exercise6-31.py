"""
6.31. Exemplo de dicionário sem valor padrão
"""

palavra = "abracadabra"
d = {}

for letra in palavra:
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1

print(d)
