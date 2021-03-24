"""
5.11. Acumuladores
"""


def acumuladoresV1():
    n = 1
    soma = 0

    while n <= 10:
        x = int(input(f"Digite o {n}º número: "))
        soma += x
        n += 1

    print(f"Soma: {soma}")


def acumuladoresV2():
    x = 1
    soma = 0

    while x <= 5:
        n = int(input(f"{x}. Digite o número: "))
        soma += n
        x += 1

    print(f"Média: {soma / 5:5.2f}")


acumuladoresV1()
