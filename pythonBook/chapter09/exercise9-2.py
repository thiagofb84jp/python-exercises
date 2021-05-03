# 9.2. Abrindo, lendo e fechando um arquivo

arquivo = open("fileForRead.txt", "r")

for linha in arquivo.readlines():
    print(linha)

arquivo.close()
