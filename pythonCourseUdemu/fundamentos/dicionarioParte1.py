# Dicionário
# Trata-se de uma estrutura chave/valor
# Lembrando: não é semelhante a estrutura de objetos que tem-se em Javascript

pessoa = {'nome': 'Prof(a). Ana',
          'idade': 38,
          'cursos': ['Inglês', 'Português']}

print(type(pessoa))
print(dir(dict))
print(len(pessoa))

print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))
