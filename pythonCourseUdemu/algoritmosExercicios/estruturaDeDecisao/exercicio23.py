"""
23. Faça um Programa que peça um número e
        informe se o número é inteiro ou decimal.
            Dica: utilize uma função de arredondamento.
"""

numero = 38.65

if (numero == round(numero)):
    print("Inteiro.")
else:
    print("Decimal.")
    print("Arredondado para baixo: ", round(numero - 0.5))
    print("Arredondado para cima: ", round(numero + 0.5))
