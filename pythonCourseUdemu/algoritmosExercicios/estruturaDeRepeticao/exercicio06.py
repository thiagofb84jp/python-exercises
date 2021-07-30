"""
6. Faça um programa que imprima na tela os números de 1 a 20,
   um abaixo do outro. Depois modifique o programa para que ele
   mostre os números um ao lado do outro.
"""

print("Iterando com os números: ")
for i in range(1, 21):
    print(i)

print("Exibindo-os lado a lado: ")
print(list(range(1, 21)))
