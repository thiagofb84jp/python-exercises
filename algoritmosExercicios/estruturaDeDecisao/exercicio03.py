"""
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

sexo = "f".upper()

if (sexo == "M"):
    print("Sexo {} = Masculino".format(sexo))
elif (sexo == "F"):
    print("Sexo {} = Feminino".format(sexo))
else:
    print("Sexo inválido.")
