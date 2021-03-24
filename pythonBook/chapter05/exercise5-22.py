'''
5.22. 
'''

aPagar = 0

while True:
    codigo = int(input("Código da mercadoria (0 para sair): "))
    preco = 0

    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1.00
    elif codigo == 3:
        preco = 4.00
    elif codigo == 5:
        preco = 7.00
    elif codigo == 9:
        preco = 8.00
    else:
        print("Código inválido!")

    if preco != 0:
        quantidade = int(input("Quantidade: "))
        aPagar = aPagar + (preco * quantidade)

print(f"Total a pagar R${aPagar:8.2f}")
