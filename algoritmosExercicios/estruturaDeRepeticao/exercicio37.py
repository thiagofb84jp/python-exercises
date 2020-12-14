"""
37. Uma academia deseja fazer um senso entre seus clientes
    para descobrir o mais alto, o mais baixo, a mais gordo e
    o mais magro, para isto você deve fazer um programa que pergunte
    a cada um dos clientes da academia seu código, sua altura e seu peso.
"""

codClientes = []
alturaClientes = []
pesoClientes = []
numeroCliente = 1
codigo = True

while (codigo != 0):
    print("\nCliente nº ", numeroCliente)
    codigo = int(input("Digite o código: "))
    if (codigo == 0):
        break
    else:
        altura = float(input("Digite a altura: "))
        peso = float(input("Digite o peso: "))
        codClientes.append(codigo)
        alturaClientes.append(altura)
        pesoClientes.append(peso)
        numeroCliente += 1

codMagro = pesoClientes.index(min(pesoClientes))
codGordo = pesoClientes.index(max(pesoClientes))
codAlto = alturaClientes.index(max(alturaClientes))
codBaixo = alturaClientes.index(min(alturaClientes))

print("\n" * 5)

print("Código do mais magro: ", codClientes[codMagro])
print("Código do mais gordo: ", codClientes[codGordo])
print("Código do mais alto: ", codClientes[codAlto])
print("Código do mais baixo: ", codClientes[codBaixo])
print("Média de altura: ", sum(alturaClientes) / len(alturaClientes))
print("Média de peso: ", sum(pesoClientes) / len(pesoClientes))
