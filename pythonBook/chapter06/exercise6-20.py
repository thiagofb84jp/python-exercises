"""
6.20. Estrutura de repetição 'For'
"""

L = []

while True:
    n = int(input("Digite um número (0 para sair do programa): "))
    if n == 0:
        break
    L.append(n)

for e in L:
    print(e)
