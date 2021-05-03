# 9.3. Abrindo, lendo e fechando um arquivo com 'with'

with open("fileForRead.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
