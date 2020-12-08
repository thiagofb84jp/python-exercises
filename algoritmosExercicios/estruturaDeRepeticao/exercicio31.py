"""
31. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de
    1,99 e agora possui uma loja de conveniências. Faça um programa que implemente
    uma caixa registradora rudimentar.
"""


def clear():
    print("\n" * 40)


while (True):
    print("------------------- Lojas Tabajara -------------------")
    numero = 1
    total = 0

    while (True):
        preco = float(input("Produto {}: R$ ".format(numero)))
        numero += 1
        total += preco
        if (preco == 0):
            break

    print("-------------------------------------------------------")
    reset = input("Pressione 0 para reset, 1 para encerrar: ")
    if (reset == "0"):
        clear()
        continue
    else:
        clear()
        print("Encerrando caixa....")
        break
