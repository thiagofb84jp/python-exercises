# 8.34.1. Tratando exceções de forma específica
nomes = ["Ana", "Carlos", "Maria"]
for tentativa in range(3):
    try:
        i = int(input("Digite o índice que quer imprimir: "))
        print(nomes[i])
    except ValueError:
        print("Digite um número!")
    finally:
        print(f"Tentativa {tentativa + 1}")
