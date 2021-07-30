"""
13. Faça um programa que peça dois números, base e expoente,
    calcule e mostre o primeiro número elevado ao segundo número.
"""

base = 3
expoente = 3
potencia = 1

for i in range(expoente):
    potencia *= base
    i += 1

print(base, "^", expoente, "=", potencia)
