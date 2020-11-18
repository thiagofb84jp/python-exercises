"""
15. Faça um Programa que peça os 3 lados de um triângulo.
      O programa deverá informar se os valores podem ser um triângulo.
        Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
            isósceles ou escaleno.
"""

ladoA = 5
ladoB = 5
ladoC = 5

if ((ladoA + ladoB) < ladoC) or ((ladoA + ladoC) < ladoB) or ((ladoB + ladoC) < ladoA):
    print("Não é um triângulo!")
elif (ladoA == ladoB) and (ladoA == ladoC):
    print("É um triângulo Equilátero!")
elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
    print("É um triângulo Isóceles!")
else:
    print("É um triângulo Escaleno!")
