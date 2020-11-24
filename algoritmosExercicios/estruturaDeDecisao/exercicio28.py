'''
28. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
'''

quantidadeMorango = 10
quantidadeMaca = 2

if (quantidadeMorango <= 5):
    precoMorango = quantidadeMorango * 2.50
else:
    precoMorango = quantidadeMorango * 2.20

if (quantidadeMaca <= 5):
    precoMaca = quantidadeMaca * 1.80
else:
    precoMaca = quantidadeMaca * 1.50

precoTotalFrutas = precoMorango + precoMaca
quantidadeTotalFrutas = quantidadeMorango + quantidadeMaca

if ((quantidadeTotalFrutas >= 8) or (precoTotalFrutas > 25.00)):
    desconto = ((precoTotalFrutas * 10) / 100)
    valorTotal = precoTotalFrutas - desconto
else:
    valorTotal = precoTotalFrutas

print("\n************************** CUPOM FISCAL **************************")
print("Quantidade de morangos: {}".format(quantidadeMorango))
print("Quantidade de maçãs: {}".format(quantidadeMaca))
print("Valor total: {:.2f}".format(valorTotal))
print("*********************************************************************")
