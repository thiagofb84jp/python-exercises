'''
6.6. Adição de elementos à lista
'''

L = []

while True:
    n = int(input("Digite um número: ('0' para sair): "))
    if n == 0:
        print("Saindo do programa...")
        break
    L.append(n)

x = 0
while x < len(L):
    print(L[x])
    x += 1

print(f"Lista completa: {L}")
