'''
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
    caso o valor seja inválido e continue pedindo até que o usuário informe
    um valor válido.
'''

nota = float(input("Informe uma nota de 0 a 10: "))

while ((nota > 10) or (nota < 0)):
    print("Nota diferente de 0 a 10. Por favor, informe novamente.")
    nota = float(input("Informe um número de 0 a 10: "))

print("Fim do programa.")
