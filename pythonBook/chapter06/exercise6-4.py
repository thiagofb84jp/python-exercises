"""
6.1. Cálculo da média com as notas digitadas
"""

notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < len(notas):
    notas[x] = float(input(f"Nota {x + 1}: "))
    soma += notas[x]
    x += 1
print("")

x = 0
while x < len(notas):
    print(f"Nota {x + 1}: {notas[x]:6.2f}")
    x += 1

print(f"Média: {soma / x:5.2f}")
