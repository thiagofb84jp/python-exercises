# 8.45. Imprimindo os elementos de uma lista

ESPACOS_POR_NIVEL = 4


def imprimeElementos(l, nivel=0):
    espacos = ' ' * ESPACOS_POR_NIVEL * nivel

    if type(l) == list:
        print(espacos, "[")
        for e in l:
            imprimeElementos(e, nivel + 1)
        print(espacos, "]")
    else:
        print(espacos, l)


L = [1, [2, 3, 4, [5, 6, 7]]]

imprimeElementos(L)
