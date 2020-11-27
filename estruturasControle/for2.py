# For - Parte 2

palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end='\n')

print("\nFim.\n")

aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria\n']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

diasSemana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta',
              'Sexta', 'Sábado')

for dia in diasSemana:
    print(f'Hoje é {dia}')

# Continuar com a parte de 'For' letra
