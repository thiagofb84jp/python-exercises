# Leitura Stream #02
arquivo = open('pessoas.csv')

for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()
