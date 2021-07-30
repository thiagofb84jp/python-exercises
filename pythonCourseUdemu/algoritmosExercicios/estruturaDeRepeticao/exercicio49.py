'''
49. Faça um programa que mostre os n termos da Série
    a seguir:
'''

n1 = 1
n2 = 1
n1Lista = []
n2Lista = []

print("S = ", end="")

while (n1 <= 10 - 1):
    print(n1, "/", n2, " + ", end="")
    n1Lista.append(n1)
    n2Lista.append(n2)
    n1 += 1
    n2 += 2

print(n1, "/", n2, " = ", sum(n1Lista), "/", sum(n2Lista))
