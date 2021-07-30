'''
25. Faça um programa que peça para n pessoas a sua idade,
    ao final o programa devera verificar se a média de idade da
    turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
    dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''

nPessoas = int(input("Digite o número de pessoas que informarão a idade: "))
lista = []

for i in range(nPessoas):
    idade = lista.append(int(input("Digite a idade: ")))

if sum(lista) / len(lista) < 25:
    print("Jovem")
elif sum(lista) / len(lista) >= 25 and sum(lista):
    print("Adulto")
else:
    print("Idosa")
