# 8.35.1. Tratando exceções com 'raise'
nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
        raise
    except IndexError:
        print("Valor inválido! Digite entre -3 e 3")
    finally:
        print("Sempre o finally é executado.")
