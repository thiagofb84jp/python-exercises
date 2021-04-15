# Funções

# Função que não retorna nenhum valor
def somaSemRetorno(a, b):
    print(a + b)


# Função que retorna um valor
def somaComRetorno(a, b):
    return a + b


# Função na qual retorna se um número é PAR ou ÍMPAR
def parOuImpar(x):
    if x % 2 == 0:
        print(f"{x} é um número par.")
    else:
        print(f"{x} é um número ímpar.")


somaSemRetorno(1, 27)
print(somaComRetorno(5, 7))
parOuImpar(10)
parOuImpar(55)
