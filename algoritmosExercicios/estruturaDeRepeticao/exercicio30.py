"""
30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora
    e pretende implantar a metodologia da tabelinha, que já é um sucesso
    na sua loja de 1,99.
"""

paes = int(input("Digite a quantidade de pães: "))
while(paes > 50):
    produtos = int(input("Digite a quantidade de produtos [menor que 50]:"))

count = 1
precoPao = float(input("Qual o preço do pão? "))

for i in range(paes):
    print(count, "= R$", round(precoPao * count, 2))
    count += 1
