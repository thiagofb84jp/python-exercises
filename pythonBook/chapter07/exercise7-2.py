"""
7.2. Lendo duas strings e encontrando a posição de ambas
"""

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

posicao = primeira.find(segunda)

if posicao == -1:
    print(f"'{segunda}' não encontrada em '{primeira}'")
else:
    print(f"{segunda} encontrada na posição {posicao} de {primeira}")
