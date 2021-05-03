# 9.9. Extraindo os múltiplos de 4 no arquivo 'pares.txt'

with open("multiplos de 4.txt", "w") as multiplos4:
    with open("pares.txt") as pares:
        for line in pares.readlines():
            if int(line) % 4 == 0:
                multiplos4.write(line)
