# For - Parte 2

palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end='\n')

print("\nFim da primeira iteração.\n")

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria\n']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

diasSemana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta',
              'Sexta', 'Sábado')

for dia in diasSemana:
    print(f'Hoje é {dia}')

for letra in set('muito legal'):
    print(letra)

print()

for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)
