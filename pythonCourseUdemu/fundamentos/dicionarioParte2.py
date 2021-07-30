# Dicionário

pessoa = {'nome': 'Prof(o). Alberto',
          'idade': 43,
          'cursos': ['React', 'Python']}

print(pessoa)
pessoa['idade'] = 44
pessoa['cursos'].append('Angular')
print(pessoa)
pessoa.pop('idade')

print(pessoa)
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)
