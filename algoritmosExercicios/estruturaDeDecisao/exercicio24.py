"""
24. Faça um Programa que leia 2 números e
    em seguida pergunte ao usuário qual operação
    ele deseja realizar.
"""

x = 5
y = 4

operacao = "+"

if (operacao == "+"):
    resultado = x + y

    if ((resultado % 2) == 0):
        print("O número {} é par.".format(resultado))
    else:
        print("O número {} é ímpar.".format(resultado))

    if (resultado >= 0):
        print("O número {} é positivo.".format(resultado))
    else:
        print("O número {} é negativo.".format(resultado))

    if (round(resultado) == resultado):
        print("O número {} é inteiro.".format(resultado))
    else:
        print("O número {} é decimal.".format(resultado))

if (operacao == "-"):
    resultado = x - y

    if ((resultado % 2) == 0):
        print("O número {} é par.".format(resultado))
    else:
        print("O número {} é ímpar.".format(resultado))

    if (resultado >= 0):
        print("O número {} é positivo.".format(resultado))
    else:
        print("O número {} é negativo.".format(resultado))

    if (round(resultado) == resultado):
        print("O número {} é inteiro.".format(resultado))
    else:
        print("O número {} é decimal.".format(resultado))

if (operacao == "*"):
    resultado = x * y

    if ((resultado % 2) == 0):
        print("O número {} é par.".format(resultado))
    else:
        print("O número {} é ímpar.".format(resultado))

    if (resultado >= 0):
        print("O número {} é positivo.".format(resultado))
    else:
        print("O número {} é negativo.".format(resultado))

    if (round(resultado) == resultado):
        print("O número {} é inteiro.".format(resultado))
    else:
        print("O número {} é decimal.".format(resultado))

if (operacao == "/"):
    resultado = x / y

    if ((resultado % 2) == 0):
        print("O número {} é par.".format(resultado))
    else:
        print("O número {} é ímpar.".format(resultado))

    if (resultado >= 0):
        print("O número {} é positivo.".format(resultado))
    else:
        print("O número {} é negativo.".format(resultado))

    if (round(resultado) == resultado):
        print("O número {} é inteiro.".format(resultado))
    else:
        print("O número {} é decimal.".format(resultado))
