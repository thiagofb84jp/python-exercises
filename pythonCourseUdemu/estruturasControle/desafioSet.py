# Desafio Set

PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'João gosta de futebol e política.',
    'A praia foi divertida.',
    'Maria possui possui religião evangélica.',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("Texto possui palavras proibidas: ", intersecao)
    else:
        print("Texto autorizado: ", texto)
