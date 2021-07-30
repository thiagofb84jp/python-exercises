"""
36. Desenvolva um programa que faça a tabuada de um número
    qualquer inteiro que será digitado pelo usuário, mas a tabuada
    não deve necessariamente iniciar em 1 e terminar em 10, o valor
    inicial e final devem ser informados também pelo usuário
"""

numeroTabuada = int(input("Qual tabuada você gostaria de visualizar? "))

numeroInicial = int(input("Iniciar a tabuada no nº: "))
while(numeroInicial < 1):
    numeroInicial = int(
        input("Por favor, informe um número maior que 1: "))

numeroFinal = int(input("Finalizar a tabuada no nº: "))
while(numeroFinal > 10):
    numeroFinal = int(input("Por favor, informe um número menor que 10: "))

if (numeroFinal < numeroInicial):
    print("O valor inicial precisa ser maior do que o valor final")
    print("Fim do programa.")
else:
    caminho = numeroInicial

    for i in range(numeroInicial, numeroFinal + 1):
        print(numeroTabuada, " X ", caminho, " = ", numeroTabuada * caminho)
        caminho += 1
