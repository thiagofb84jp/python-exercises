# 8.8. Cálculo do Fatorial

def fatorial(n):
    fat = 1

    while n > 1:
        fat *= n
        n -= 1

    return fat


print(fatorial(3))
print(fatorial(1))
print(fatorial(5))
print(fatorial(0))
