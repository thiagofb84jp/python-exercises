# For - Parte 4

# for i in range(1, 11):
#     if (i == 6):
#         break
#     print(i)
# else:
#     print("Fim!")

# Função sortearDado números entre 1 e 6
# For com range de 1 a 6
# Se for ímpar continue
# Se o número for par e for igual ao valor sorteado
# Pela função dado imprimir 'ACERTOU' e depois chamar o break
# Se não acertar chamar o else... print('Não acertou o número!')

from random import randint


def sortearDado():
    return randint(1, 6)


for i in range(1, 7):
    if ((i % 2) == 0):
        continue

    if sortearDado() == i:
        print('ACERTOU!', i)
        break
else:
    print('Não acertou o número!')
