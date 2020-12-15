"""
43. Faça um programa que leia o código dos
    itens pedidos e as quantidades desejadas. Calcule
    e mostre o valor a ser pago por item (preço * quantidade)
    e o total geral do pedido.
"""

codigos = [100, 101, 102, 103, 104, 105]
precos = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
codigo = True
numeroPedido = 1
pedido = []

while (codigo != 0):
    print("\nPedido nº ", numeroPedido)
    codigo = int(input("Digite o código do alimento: "))
    if (codigo == 0):
        break
    else:
        while (codigo not in codigos):
            print("[Este código não corresponde a nenhum alimento.]")
            codigo = int(
                input("Por favor, digite um código válido de alimento: "))

        indice = codigos.index(codigo)
        quantidade = int(input("Digite a quantidade: "))
        valorPedido = precos[indice] * quantidade
        pedido.append(valorPedido)
    numeroPedido += 1

pedidoNota = 0
print("\n" * 2)

for i in range(numeroPedido - 1):
    print("Pedido nº ", pedidoNota + 1, " = R$", round(pedido[pedidoNota], 2))
    pedidoNota += 1

print("Total: R$ ", round(sum(pedido), 2))
