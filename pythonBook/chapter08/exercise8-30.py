# Desempacotamento de parâmetros

# 8.30.1 Função soma com número indeterminado de parâmetros
def soma(*args):
    s = 0

    for x in args:
        s += x

    return s


print(soma(1, 2))
print(soma(2))
print(soma(5, 6, 7, 8))
print(soma(9, 10, 20, 30, 40))

print()


# 8.30.2. Função imprimeMaior com número indeterminado de parâmetros
def imprimeMaior(mensagem, *numeros):
    maior = None

    for e in numeros:
        if maior is None or maior < e:
            maior = e

    print(mensagem, maior)


imprimeMaior("Maior: ", 5, 4, 3, 2, 1)
imprimeMaior("Maior: ", *[1, 7, 9])
