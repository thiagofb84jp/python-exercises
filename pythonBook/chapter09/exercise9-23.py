# 9.23. Criando novos diretórios

import os
os.mkdir("d")
os.mkdir("e")
os.mkdir("f")
print(os.getcwd())
os.chdir("d")
print(os.getcwd())
os.chdir("../e")
print(os.getcwd())
print(os.chdir(".."))
print(os.getcwd())
print(os.chdir("f"))
print(os.getcwd())
