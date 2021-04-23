# 8.41. Adivinhando o número (com 3 tentativas)

import random

n = random.randint(1, 10)

for tentativa in range(3):
    x = int(input("Escolha um número entre 1 e 10: "))

    if x == n:
        print("Você acertou! :)")
        break
    else:
        print("Você errou. :(")

    print(f"Tentativa nº {tentativa + 1}")
