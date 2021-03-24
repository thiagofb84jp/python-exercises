'''
5.14. Tabuada (a cargo do usuário)
'''

n = int(input("Tabuada de: "))
inicio = int(input("Informe o início: "))
fim = int(input("Informe o final: "))

x = inicio

while x <= fim:
    print(f"{n} X {x} = {n * x}")
    x += 1
