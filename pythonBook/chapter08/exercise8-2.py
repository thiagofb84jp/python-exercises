# Funções

# Função na qual utiliza o enumerate em uma lista
def enum(lista):
    for x, e in enumerate(lista):
        x += 1
        print(f"[{x}] {e}")
    print()


A = [5, 9, 13]
enum(A)


# Função na qual pesquisa em uma lista
def pesquise(lista, valor):
    for x, e in enumerate(lista):
        x += 1
        if e == valor:
            return x

    return None


# Função na qual calcula a média dos valores em uma lista
def soma(L):
    total = 0
    for e in L:
        total += e

    return total


def media(L):
    return soma(L) / len(L)


L = [10, 20, 25, 30]

print(pesquise(L, 10))
print(pesquise(L, 20))
print(pesquise(L, 25))
print(pesquise(L, 50))
