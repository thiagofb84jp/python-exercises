# Exceções

# 8.32.1. Tratando exceções de forma específica
nomes = ["Ana", "Carlos", "Maria"]

for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    except IndexError:
        print("Valor inválido, digite entre -3 e 3.")
