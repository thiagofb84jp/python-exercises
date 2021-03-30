"""
6.15. Percorrendo listas usando 'For'
"""

L = [7, 9, 10, 12]
p = int(input("Digite um número a pesquisar: "))

for e in L:
    if e == p:
        print("Elemento encontrado!")
        break
    else:
        print("Elemento não encontrado!")
        print(f"Foi encontrado o elemento {e}")

print("\nEncerrando o programa...")
