# 9.24. Criando subdiretórios com o comando 'makedirs'

# Criando novos subdiretórios de uma só vez
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
