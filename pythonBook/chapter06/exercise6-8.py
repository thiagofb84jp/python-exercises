'''
6.8. Gerando terceira lista de elementos
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

terceira = primeira[:]
terceira.extend(segunda)

x = 0
while x < len(terceira):
    print(f"{x}: {terceira[x]}")
    x += 1

print(f"Terceira lista completa: {terceira}")
