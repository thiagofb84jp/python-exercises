"""
7. Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

x = 100
y = 20
z = 10

# Para o número maior
if (x > y) and (x > z):
    print('{} é maior que {} e {}'.format(x, y, z))
elif (y > x) and (y > z):
    print('{} é maior que {} e {}'.format(y, x, z))
else:
    print('{} é maior que {} e {}'.format(z, x, y))

# Para o número menor
if (x < y) and (x < z):
    print('{} é menor que {} e {}'.format(x, y, z))
elif (y < x) and (y < z):
    print('{} é menor que {} e {}'.format(y, x, z))
else:
    print('{} é menor que {} e {}'.format(z, x, y))
