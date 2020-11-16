# Tuplas
# A tupla é uma estrutura que não pode ser modificada
# Enquanto que a lista pode ser modificada

tupla = tuple()
tupla = ()
print(type(tupla))
print(dir(tupla))
print(help(tuple))
print(type(tupla))

tupla = ('um', )
print(tupla)
print(type(tupla))
print(tupla[0])

cores = ('verde', 'amarelo', 'azul', 'azul', 'branco', 'cinza')
print(cores)
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.index('azul'))
print(len(cores))
