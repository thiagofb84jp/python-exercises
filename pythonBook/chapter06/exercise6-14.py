"""
6.14. Estrutura de repetição 'For'
"""

# Usando 'For'
L = [8, 9, 15]
print("Usando 'For'")
for e in L:
    print(e)

# Usando 'while'
L = [8, 9, 15]
x = 0
print("\nUsando 'While'")
while x < len(L):
    e = L[x]
    print(e)
    x += 1

# Usando 'Range' com apenas um parâmero
print("\nUsando 'Range' com apenas um parâmetro")
for v in range(10):
    print(v)

# Usando 'Range' com dois parâmetros
print("\nUsando 'Range' com dois parâmetros")
for v in range(5, 8):
    print(v)

# Usando 'Range' com valores específicos
print("\nUsando 'Range' com valores específicos")
for t in range(3, 33, 3):
    print(t, end=" ")
print()

# Transformando um range em uma lista
print("\nTransformando Range em uma lista")
L = list(range(100, 1100, 50))
print(L)

# Enumerate
L = [5, 9, 13]
x = 0
print("\nEnumerate (1)")
for e in L:
    print(f"[{x}] {e}")
    x += 1

# Enumerate
L = [5, 9, 13]
print("\nEnumerate (1)")
for x, e in enumerate(L):
    print(f"[{x}] {e}")
