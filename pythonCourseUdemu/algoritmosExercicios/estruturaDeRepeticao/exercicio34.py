"""
34. Os números primos possuem várias aplicações dentro da Computação,
    por exemplo na Criptografia.
"""

numero = int(input("Digite um número: "))

if ((numero % 2 == 0) and (numero != 2)):
    print("Não é um número primo.")
else:
    print("É um número primo.")
