'''
6.9. Percorrendo duas listas e gerando uma terceira sem elementos repetidos
'''

primeira = []
segunda = []

while True:
    e = int(input("Digite um valor para a primeira lista (0 para terminar): "))
    if e == 0:
        print("Terminando a primeira lista...")
        break
    primeira.append(e)

while True:
    e = int(input("Digite um valor para a segunda lista (0 para terminar): "))
    if e == 0:
        print("Terminando a segunda lista...")
        break
    segunda.append(e)

terceira = []

duasListas = primeira[:]
duasListas.extend(segunda)

x = 0
while x < len(duasListas):
    y = 0
    while y < len(terceira):
        if duasListas[x] == terceira[y]:
            break
        y += 1
    if y == len(terceira):
        terceira.append(duasListas[x])
    x += 1

x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x += 1

print(f"Terceira lista completa: {terceira}")
