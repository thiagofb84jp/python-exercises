# 8.8. Outra forma de realizar o cálculo do Fatorial

def fatorial(n):
    fat = 1
    x = 1

    while x <= n:
        fat *= x
        x += 1

    return fat


print(fatorial(3))
print(fatorial(1))
print(fatorial(5))
print(fatorial(0))
