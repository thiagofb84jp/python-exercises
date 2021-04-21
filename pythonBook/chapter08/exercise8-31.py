# Funções Lambda

# 8.31.1. Função lambda que recebe um valor e retorna o dobro dele
a = lambda x: x * 2
print(a(3))


# 8.31.2. Função lambda que recebe mais de um parâmetro
aumento = lambda a, b: (a * b / 100)
print(aumento(100, 5))


# 8.31.3. Função lambda para somar dois números
soma = lambda x, y: (x + y)
print(soma(5, 10))


# 8.31.4. Função lambda para verificar o maior número
menor = lambda a, b: a if a < b else b
print(menor(5, 10))
print(menor(10, 2))


# 8.31.5. Função lambda adaptada para a função 'sort'
L = ["A", "b", "C", "d", "E"]
L.sort()
print(L)

L.sort(key=lambda k: k.lower())
print(L)
