# 8.24. Passando funções como parâmetro de outra


# Funções como parâmetro
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    return a / b


def imprime(a, b, foper):
    print(foper(a, b))


imprime(5, 10, soma)
imprime(10, 1, subtracao)
imprime(5, 2, multiplicacao)
imprime(10, 5, divisao)
