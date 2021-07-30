"""
1. João Papo-de-Pescador, homem de bem, comprou um microcomputador para
    controlar o rendimento diário de seu trabalho.
"""

peso = 51

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print("Excesso de peso foi de {:.2f} Kg. A multa é de R$ {:.2f}"
          .format(excesso, multa))
else:
    excesso = 0
    multa = 0
    print("Não houve excesso de peso. Portanto, não paga multa.")
