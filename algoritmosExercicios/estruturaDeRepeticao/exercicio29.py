"""
29. O Sr. Manoel Joaquim possui uma grande loja de artigos
    de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo
    de quanto cada cliente deve pagar ele desenvolveu um tabela
    que contém o número de itens que o cliente comprou e ao lado
    o valor da conta.
"""

produtos = int(input("Digite a quantidade de produtos: "))
while(produtos > 50):
    print("A quantidade de produtos tem que ser menor que 50.")
    produtos = int(input("Por favor, digite uma quantidade menor que 50: "))

precos = []
numeroProduto = 1
count = 0

for i in range(produtos):
    print("Produto nº: ", numeroProduto)
    preco = precos.append(float(input("Digite o preço do produto: ")))
    numeroProduto += 1

numeroProduto = 1
for i in range(produtos):
    print("Produto nº: ", numeroProduto, "= ", precos[count])
    count += 1
    numeroProduto += 1
