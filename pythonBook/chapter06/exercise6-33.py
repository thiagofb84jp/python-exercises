"""
6.33. Exemplo de dicionário com estoque e operação de vendas
"""

estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}
total = 0
print("Vendas:\n")

while True:
    produto = input("Nome do produto: (fim para sair): ")
    if produto == "fim":
        print("Encerrando o programa...")
        break
    if produto in estoque:
        quantidade = int(input("Quantidade: "))
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo: 6.2f}")
            estoque[produto][0] -= quantidade
            total += custo
        else:
            print("Quantidade solicitada não disponível.")
    else:
        print("Nome do produto inválido.")
print(f" Custo total: {total:21.2f}\n")
print("Estoque:\n")

for chave, dados in estoque.items():
    print("Descrição: ", chave)
    print("Quantidade: ", dados[0])
    print(f"Preço: {dados[1]:6.2f}\n")
