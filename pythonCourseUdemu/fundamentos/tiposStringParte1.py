# Tipos String - Parte 1
print(dir())
nome = 'Josefa Vieira Lima da Silva'
print(nome)
nome[0]
# Lembre-se a String é imutável. O que é possível é alterar seu valor.
# nome[0] = 'P'
# print('marca d'agua') -> erro de sintaxe
print("Dias D'Avila" == 'Dias D\'Avila')
print("Teste \" funciona!")

texto = 'Texto entre apóstrofos pode ter "aspas"'
print(texto)

doc = """Texto com múltiplas
    ... linhas"""
print(doc)

print('Texto com múltiplas \n\t... linhas')
print(doc)

doc2 = '''Também é possível
    ... com 3 aspas simples'''
print(doc2)
