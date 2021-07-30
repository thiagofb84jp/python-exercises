'''
19. Altere o programa anterior para que ele
    aceite apenas números entre 0 e 1000.
'''

lista = []
count = 0

quantidade = int(input("Digite a quantidade de números que deseja informar:"))
while (quantidade != count):
    numero = float(input("Digite um número: "))

    while (numero > 1000) or (numero < 1):
        print("Fora do intervalo permitido.")
        numero = float(input("Digite um número (entre 1 a 1000): "))

    lista.append(numero)
    count += 1

print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))
