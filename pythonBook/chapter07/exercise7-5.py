"""
7.5. Lendo uma string e imprimindo quantas vezes o caractere aparece
"""

sequencia = input("Digite a string: ")

contador = {}

for letra in sequencia:
    contador[letra] = contador.get(letra, 0) + 1

for chave, valor in contador.items():
    print(f"{chave}: {valor}x")
