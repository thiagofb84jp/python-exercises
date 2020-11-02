# Mais Operadores

# Operadores de Membro
lista = [1, 2, 3, 'Ana', 'Carla']
print(2 in lista)
print('Ana' not in lista)

# Operador de Identidade
x = 3
y = x
z = 3
print(x is y)
print(y is z)
print(x is not z)

listaA = [1, 2, 3]
listaB = listaA
listaC = [1, 2, 3]

print(listaA is listaB)
print(listaB is listaC)
print(listaA is not listaC)
