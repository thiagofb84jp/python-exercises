# 9.1. Abrindo, escrevendo e fechando um arquivo

arquivo = open("numeros.txt", "w")

for linha in range(1, 101):
    arquivo.write(f"{linha}\n")

arquivo.write("Fim da escrita dentro do arquivo.")

arquivo.close()
print("Fim do programa.")
