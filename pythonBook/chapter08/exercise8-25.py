# 8.25. Configurando funções

def imprimeLista(L, fImpresao, fCondicao):
    for e in L:
        if fCondicao(e):
            fImpresao(e)


def imprimeElemento(e):
    print(f"Valor: {e}")


def ehPar(x):
    return x % 2 == 0


def ehImpar(x):
    return not ehPar(x)


L = [1, 7, 9, 2, 11, 0]

imprimeLista(L, imprimeElemento, ehPar)
imprimeLista(L, imprimeElemento, ehImpar)
