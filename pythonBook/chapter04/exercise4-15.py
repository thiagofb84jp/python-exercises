"""
4.15. Calcular preço energia elétrica
"""

consumo = int(input("Consumo em Kwh: "))
tipo = input("Tipo da instalação (R, C ou I): ")

if tipo == "R":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "I":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
else:
    preco = 0
    print("Erro! Tipo de instalação desconhecido!")

custo = consumo * preco
print(f"Valor a pagar: R$ {custo:7.2f}")
