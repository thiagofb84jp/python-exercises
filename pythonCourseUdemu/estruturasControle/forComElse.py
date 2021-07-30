# For com Else

PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política.',
    'A praia foi divertida.',
    'Maria possui possui religião evangélica.',
]

for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida: ', palavra)
            break
    else:
        print('Texto autorizado:', texto)
