"""
6.34. Dicionário de caracteres
"""

# frase = input("Digite uma frase para contar as letras: ")
d = {}

while True:
    frase = input("Digite uma frase para contar as letras ('fim' para sair): ")
    if frase == "fim":
        print("Encerrando o programa...")
        break
    for letra in frase:
        d[letra] = d.get(letra, 0) + 1

    print(d)
