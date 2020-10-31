# Operadores Lógicos
print('>>Aula sobre Operadores Lógicos')
print(True or False)
print(7 != 3 and 2 > 3)

# Tabela Verdade do AND
print('>>Tabela verdade do AND')
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Tabela Verdade do OR
print('>>Tabela verdade do OR')
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Tabela Verdade do XOR
print('>>Tabela verdade do XOR')
print(True != True)
print(True != False)
print(False != True)
print(False != False)

# Operador de Negação (unário)
print('>>Operador de Negação (unário)')
print(not True)
print(not False)

# Algumas curiosidades
print('>>Algumas curiosidades')
print(not 0)
print(not 1)
print(not not -1)
print(not not True)

# Cuidado (ao trabalhar com operadores bit a bit)!
print('>>Cuidado (ao trabalhar com operadores bit a bit)!')
print(True & False)
print(False | True)
print(True ^ False)

# Um pouco de realidade
print('>>Um pouco de realidade no uso dos operadores binários')
saldo = 1000
salario = 4000
despesas = 3900

saldoPositivo = saldo > 0
despesasControladas = salario - despesas >= 0.2 * salario

meta = saldoPositivo and despesasControladas
print(meta)
