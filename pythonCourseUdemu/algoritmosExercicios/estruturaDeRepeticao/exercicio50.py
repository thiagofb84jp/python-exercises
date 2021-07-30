'''
50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N,
    Faça um programa que calcule o valor de H com N termos.
'''

h = 1
n = 2
hLista = []
nLista = []

print("H = 1 + ", end="")

while (n <= 10 - 1):
    print(" ", h, "/", n, " + ", end="")
    hLista.append(h)
    nLista.append(n)
    n += 1

print(h, "/", n, " => ", sum(hLista), "/", sum(nLista),
      " => ", round(sum(hLista) / sum(nLista)), 2)
