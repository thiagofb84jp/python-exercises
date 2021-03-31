"""
6.26. Temperaturas máxima, mínima e média
"""

T = [-10, -8, 0, 1, 2, 5, -2, -4]
minima = T[0]
maxima = T[0]
soma = 0

for e in T:
    if e < minima:
        minima = e
    if e > maxima:
        maxima = e
    soma += e

print(f"Temperatura máxima: {maxima} °C")
print(f"Temperatura máxima: {minima} °C")
print(f"Temperatura média: {soma / len(T)} °C")
