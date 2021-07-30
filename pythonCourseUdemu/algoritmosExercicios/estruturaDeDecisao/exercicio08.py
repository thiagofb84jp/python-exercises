"""
8. Faça um programa que pergunte o preço de três produtos e informe qual
    produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

produtoA = 10.90
produtoB = 8.40
produtoC = 3.99

# Para o produto mais barato
if (produtoA < produtoB) and (produtoA < produtoC):
    print('Produto A é o mais barato, pois, custa {}'.format(produtoA))
elif (produtoB < produtoA) and (produtoB < produtoC):
    print('Produto B é o mais barato, pois, custa {}'.format(produtoB))
else:
    print('Produto C é o mais barato, pois, custa {}'.format(produtoC))
