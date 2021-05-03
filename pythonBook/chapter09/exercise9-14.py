# 9.14. Invertendo a ordem de impressão do arquivo 'pares.txt'

with open("pares.txt", "r") as pares, open("paresInvertido.txt", "w") as saida:
    L = pares.readlines()
    L.reverse()
    for lines in L:
        saida.write(lines)
