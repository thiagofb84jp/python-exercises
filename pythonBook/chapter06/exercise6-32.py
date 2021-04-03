"""
6.32. Exemplo de dicionário com valor padrão
"""

palavra = "abracadabra"
d = {}

for letra in palavra:
    d[letra] = d.get(letra, 0) + 1

print(d)
