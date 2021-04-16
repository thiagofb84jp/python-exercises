# 8.22. Função na qual imprime uma barra

# Função barra sem parâmetros
def barra():
    print("*" * 40)


barra()


# Função barra com parâmetros
def barraComParametros(n=100, caractere="*"):
    print(caractere * n)


barraComParametros()


# Função soma com parâmetros obrigatórios
def soma(a, b, imprime=False):
    s = a + b
    if imprime:
        print(s)
    return s


print(soma(2, 3))
print(soma(3, 4, True))
print(soma(5, 8, False))

"""
# Função soma com passagem de parâmetros inválidos
def somaComPassParamInvalido(imprime=True, a, b):
    s = a + b
    if imprime:
        print(s)
    return s


print(somaComPassParamInvalido(True, 2, 3))
print(soma(3, 4, True))
print(soma(5, 8, False))
"""
