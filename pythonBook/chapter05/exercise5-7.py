"""
5.7. Imprimindo números ímpares
"""

x = 0
fim = int(input("Digite o último número a imprimir: "))

while x <= fim:
    if (x % 2) != 0:
        print(x)
    x += 1
