'''
19. Faça um Programa que leia um número inteiro menor que 1000
    e imprima a quantidade de centenas, dezenas e unidades do mesmo.
'''

numero = 986

unidade = numero % 10

numero = (numero - unidade) / 10

dezena = numero % 10

numero = (numero - dezena) / 10

centena = numero

dezena = int(dezena)
centena = int(centena)

print("{} centena(s), {} dezena(s) e {} unidade(s)"
      .format(centena, dezena, unidade))
