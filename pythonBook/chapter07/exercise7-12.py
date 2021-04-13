# Jogo da velha

velha = """               Posições
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
"""

posicoes = [
    None,
    (5, 1),
    (5, 5),
    (5, 9),
    (3, 1),
    (3, 5),
    (3, 9),
    (1, 1),
    (1, 5),
    (5, 1),
    (1, 9)
]

ganho = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
    [7, 5, 3],
    [1, 5, 9]
]

tabuleiro = []
for linha in velha.splitlines():
    tabuleiro.append(list(linha))


# jogador = "X"  # Começa jogando com X (parou nesta linha!)
