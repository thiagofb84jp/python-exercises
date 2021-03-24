'''
5.16. Calcular valores (1)
'''

p = int(input("Primeiro número: "))
s = int(input("Segundo número: "))

x = 1
r = 0

while x <= s:
    r += p  # r = r + p
    x += 1

print(f"{p} X {s} = {r}")
