"""
5.26. Tabuada com menu
"""

while True:
    print("""

Menu
------
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair

""")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 5:
        break
    elif opcao >= 1 and opcao < 5:
        n = int(input("Tabuada de: "))
        x = 1
        while x <= 10:
            if opcao == 1:
                print(f"{x} + {n} = {x + n}")
            elif opcao == 2:
                print(f"{x} - {n} = {x - n}")
            elif opcao == 3:
                print(f"{x} X {n} = {x * n}")
            elif opcao == 4:
                print(f"{n} / {x} = {n / x:5.0f}")
            x += 1
    else:
        print("Opção inválida!")
