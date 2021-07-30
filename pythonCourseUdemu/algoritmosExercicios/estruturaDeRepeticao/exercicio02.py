"""
2. Faça um programa que leia um nome de usuário e a sua senha e não
    aceite a senha igual ao nome do usuário, mostrando uma mensagem
    de erro e voltando a pedir as informações.
"""

nome = input(("Informe seu nome de usuário: "))
senha = input(("Informe sua senha: "))

while ((nome == senha)):
    print("Seu nome é igual a sua senha.")
    print("Por favor, informe um nome diferente da senha.")
    nome = input(("Informe seu nome de usuário: "))
    senha = input(("Informe sua senha: "))

print("Seu nome: {}".format(nome))
print("Sua senha: {}".format(senha))
