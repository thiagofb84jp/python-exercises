"""
26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
"""

precoGasolina = 2.50
precoAlcool = 2.50
combustivel = 1

litros = 50.2

if (litros <= 20):
    if (combustivel == 1):
        desconto = 3 / 100
        valorTotal = (precoAlcool * litros) - desconto
    else:
        desconto = 5 / 100
        valorTotal = (precoGasolina * litros) - desconto

    if (combustivel == 2):
        desconto = 4 / 100
        valorTotal = (precoAlcool * litros) - desconto
    else:
        desconto = 6 / 100
        valorTotal = (precoGasolina * litros) - desconto

if (combustivel == 1):
    print("Álcool: R$ {}".format(precoAlcool))
else:
    print("Gasolina: R$ {}".format(precoGasolina))

print("Litros: {}".format(litros))
print("Total a pagar: {:.2f}".format(valorTotal))


"""
if (litros > 20):
    if (combustivel == 1):
        valorTotal = (precoAlcool * litros) * 0.95
    else:
        valorTotal = (precoGasolina * litros) * 0.94

    if (combustivel == 2):
        valorTotal = (precoAlcool * litros) * 0.97
    else:
        valorTotal = (precoGasolina * litros) * 0.98

if (combustivel == 1):
    print("Álcool: R$ {}".format(precoAlcool))
else:
    print("Gasolina: R$ {}".format(precoGasolina))

print("Litros: {}".format(litros))
print("Total a pagar: {:.2f}".format(valorTotal))
"""
