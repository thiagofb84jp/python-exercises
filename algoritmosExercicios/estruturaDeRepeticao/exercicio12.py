"""
12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada
    de qualquer número inteiro entre 1 a 10. O usuário deve informar
    de qual numero ele deseja ver a tabuada.
"""

numero = int(input("Digite um número: "))

for i in range(1, 11):
    tabuada = numero * i
    print(numero, " X ", i, " = ", tabuada)
    i += 1

# A mesma solução com WHILE
# contador = 1

# while (contador <= 10):
#     tabuada = numero * contador
#     print(numero, " X ", contador, " = ", tabuada)
#     contador = contador + 1
