# 9.5. Lendo um arquivo pelo terminal e imprimindo todas as linhas deste

import sys

if len(sys.argv) != 2:
    print("\nUso: exercise9-5.py nome_do_arquivo\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")

    for linha in arquivo.readlines():
        print(linha[:-1])

    arquivo.close()
