'''
5.17. Calcular valores (2)
'''

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))

quociente = 0
x = dividendo

while x >= divisor:
    x -= divisor
    quociente += 1

resto = x

print(f"{dividendo} / {divisor} = {quociente} (quociente) {resto} (resto)")
