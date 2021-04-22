# 8.37.1. Tratando exceções utilizando 'else'
while True:
    try:
        v = int(input("Digite um número inteiro (0 sai): "))
        if v == 0:
            break
    except Exception:
        print("Valor inválido! Redigite.")
    else:
        print("Parabéns, nenhuma exceção.")
    finally:
        print("Executado sempre, mesmo com break.")
