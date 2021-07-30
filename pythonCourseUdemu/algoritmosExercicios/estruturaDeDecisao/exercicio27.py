'''
27. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
'''

tipoCarne = 1
quantidade = 5
resposta = 1

if (tipoCarne == 1):
    nomeCarne = "Filé Duplo"
    if (quantidade <= 5):
        preco = quantidade * 4.90
    else:
        preco = quantidade * 5.00
elif (tipoCarne == 2):
    nomeCarne = "Alcatra"
    if (quantidade <= 5):
        preco = quantidade * 5.90
    else:
        preco = quantidade * 6.80
elif (tipoCarne == 3):
    nomeCarne = "Picanha"
    if (quantidade <= 5):
        preco = quantidade * 6.90
    else:
        preco = quantidade * 7.80

if (resposta == 1):
    r = "SIM"
    desconto = ((preco * 5) / 100)
    valorTotal = preco - desconto
else:
    r = "NÃO"
    valorTotal = preco

print("\n************************** CUPOM FISCAL **************************")
print("Carne: {}".format(nomeCarne))
print("Quantidade: {}".format(quantidade))
print("Preço: {}".format(preco))
print("A compra foi com desconto? {}".format(r))
print("Valor total: {:.2f}".format(valorTotal))
print("*********************************************************************")
