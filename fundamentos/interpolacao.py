# Interpolação

from string import Template

nome, idade = 'Ana', 30.9875
print('Nome: %s Idade: %d' % (nome, idade))

nome, idade = 'João', 30.9875
print('Nome: %s Idade: %.1f' % (nome, idade))

nome, idade = 'Karla', 30
print('Nome: {0} Idade: {1}'.format(nome, idade))

nome, idade = 'Marta', 40
print(f'Nome: {nome} Idade: {idade}')

s = Template('Nome: $nome Idade: $idade')
print(s.substitute(nome=nome, idade=idade))
