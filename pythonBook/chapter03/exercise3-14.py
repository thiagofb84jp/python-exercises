"""
3.14. Calcular quantidade de quilômetros percorridos
"""

km = int(input("Digite a quantidade de quilômetros percorridos: "))
dias = int(input("Digite quantos dias você ficou com o carro: "))

precoPorDia = 60
precoPorKm = 0.15

precoAPagar = km * precoPorKm + dias * precoPorDia

print(f"Total a pagar: {precoAPagar}")
