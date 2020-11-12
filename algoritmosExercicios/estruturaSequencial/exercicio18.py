"""
1. Faça um Programa para uma loja de tintas. O programa deverá
    pedir o tamanho em metros quadrados da área a ser pintada.
"""

tamanho = 100

litros = tamanho / 6
latas = litros / 18

if latas % 18 != 0:
    latas += 1
preco = latas * 80

galoes = litros / 3.6

if galoes % 3.6 != 0:
    galoes += 1
preco2 = galoes * 25

misturaLata = litros / 18
misturaGalao = (litros - (misturaLata * 18)) / 3.6

if litros - (misturaLata * 18) % 3.6 != 0:
    misturaGalao += 1

precoMisturaLata = misturaLata * 80
precoMisturaGalao = misturaGalao * 25

print("Apenas latas de 18 litros: {:.0f}, o preço: {:.0f}"
      .format(latas, preco))
print("Apenas galões de 3.6 litros: {:.0f}, o preço: {:.0f}"
      .format(galoes, preco2))
print("Misturas: lata {:.0f} e galão: {:.0f}"
      .format(misturaLata, misturaGalao))
print("Valores das misturas: Lata = {:.0f} e Galão = {:.0f}"
      .format(precoMisturaLata, precoMisturaGalao))
