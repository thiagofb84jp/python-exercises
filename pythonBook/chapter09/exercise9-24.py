# 9.24. Criando subdiretórios com o comando 'makedirs'

# Criando novos subdiretórios de uma só vez
import os.path
import os
os.makedirs("avô/pai/filho")
os.makedirs("avó/mãe/filha")

# Renomeando diretórios
os.mkdir("velho")
os.rename("velho", "novo")

# Usando a função 'rename' para mover arquivos
os.makedirs("grandpa/daddy/son")
os.makedirs("grandma/mom/daughter")
os.rename("grandpa/daddy/son", "grandma/mom/son")

# Cria um arquivo e o fecha imediatamente
open("moribundo.txt", "w").close()
os.mkdir("vago")
os.rmdir("vago")
os.remove("moribundo.txt")

# Exibe uma listagem (na horizontal) contendo todos os arquivos e diretórios
print(os.listdir("."))
print(os.listdir("avô"))
print(os.listdir("avô/pai"))
print(os.listdir("avó/mãe"))

# Exibe a listagem (em forma de árvore) contendo todos os diretórios
print("")
for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a}/")
    elif os.path.isfile(a):
        print(a)
