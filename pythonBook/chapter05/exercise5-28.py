"""
5.28. Imprimindo os primeiros números primos.
"""

n = int(input("Digite um número: "))
if n < 0:
    print("Número inválido. Digite apenas valores positivos.")
else:
    if n >= 1:
        print(2)
        p = 1
        y = 3
        while p < n:
            x = 3
            while x < y:
                if y % x == 0:
                    break
                x += 2
            if x == y:
                print(x)
                p += 1
            y += 2
