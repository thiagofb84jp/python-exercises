'''
5.24. Repetições Aninhadas
'''

tabuada = 1

while tabuada <= 10:
    print("Tabuada de ", tabuada)
    numero = 1
    while numero <= 10:
        print(f"{tabuada} X {numero} = {tabuada * numero}")
        numero += 1
    tabuada += 1
    print("")
