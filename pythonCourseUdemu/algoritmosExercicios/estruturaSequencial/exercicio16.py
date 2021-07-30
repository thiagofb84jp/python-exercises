"""
1. Faça um programa para uma loja de tintas. O programa
    deverá pedir o tamanho em metros quadrados da área a ser pintada.
"""

tamanho = 102
litros = tamanho / 3

if tamanho % 54 == 0:
    latas = tamanho / 54
else:
    latas = (tamanho / 54) + 1

preco = latas * 80

print("Quantidade de latas = {:.0f}".format(latas))
print("Preço = {:.2f}".format(preco))
