"""
6. Faça um Programa que leia três números e mostre o maior deles.
"""

x = 100
y = 200
z = 300

if (x > y) and (x > z):
    print('{} é maior que {} e {}'.format(x, y, z))
elif (y > x) and (y > z):
    print('{} é maior que {} e {}'.format(y, x, z))
else:
    print('{} é maior que {} e {}'.format(z, x, y))
