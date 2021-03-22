"""
3.11. Calcular o valor do desconto e o preço a pagar pela mercadoria.
"""

preco = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))

valorDesconto = preco * desconto / 100
valorAPagar = preco - valorDesconto

print(f"Um desconto de {desconto:.2f} % em uma mercadoria de R$ {preco:.2f}")
print(f"vale R$ {valorDesconto:.2f}")
print(f"O valor a pagar é de R$ {valorAPagar:.2f}")
