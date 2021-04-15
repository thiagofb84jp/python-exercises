# 8.13. Função modificada para facilitar o rastreamento

def fatorial(n):
    print(f"Calculando o fatorial de {n}")

    if n == 0 or n == 1:
        print(f"Fatorial de {n} = 1")
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f" Fatorial de {n} = {fat}")
        return fat


print(fatorial(4))
# print(fatorial(3))
# print(fatorial(1))
# print(fatorial(5))
# print(fatorial(0))
