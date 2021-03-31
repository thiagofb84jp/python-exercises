"""
6.22. Cópia de elementos para outras listas
"""

V = [9, 8, 7, 12, 0, 13, 21, 25, 10]
P = []
I = []

for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)

print("Pares: ", P)
print("Ímpares: ", I)
