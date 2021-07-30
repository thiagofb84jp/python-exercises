'''
22. Faça um Programa para um caixa eletrônico. O programa deverá perguntar
        ao usuário a valor do saque e depois informar quantas notas de
        cada valor serão fornecidas.
'''

numero = 956

cem = numero // 100
numero = numero - (cem * 100)

cinquenta = numero // 50
numero = numero - (cinquenta * 50)

dez = numero // 10
numero = numero - (dez * 10)

cinco = numero // 5
numero = numero - (cinco * 5)

um = numero

print("Notas de R$ 100,00 = ", cem)
print("Notas de R$ 50,00 = ", cinquenta)
print("Notas de R$ 10,00 = ", dez)
print("Notas de R$ 5,00 = ", cinco)
print("Notas de R$ 1,00 = ", um)
