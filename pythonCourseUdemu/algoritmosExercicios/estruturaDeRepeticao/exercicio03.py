"""
3. Faça um programa que leia e valide as seguintes informações:
"""

# Nome: Maior que 3 (três) caracteres
nome = input("Informe seu nome: ")
while ((len(nome) <= 3)):
    print("O nome não pode ser abaixo de 3 (três) caracteres.")
    nome = input("Por favor, informe um nome válido: ")

# Idade: Entre 0 a 150
idade = int(input("Informe a sua idade: "))
while ((idade < 0) or (idade > 150)):
    print("A idade nâo pode ser menor que zero e maior que 150.")
    idade = int(input("Por favor, informe uma idade válida: "))

# Salário: tem que ser acima de zero
salario = float(input("Informe o seu salário: "))
while ((salario < 0)):
    print("O salário não pode ser menor que zero.")
    salario = float(input("Por favor, informe um salário válido: "))

# Sexo ('M' ou 'F')
sexo = input("Informe seu sexo: ")
while ((sexo != 'M') and ((sexo != 'F'))):
    print("Sexo inválido (digite 'M' ou 'F')")
    sexo = input("Por favor, informe uma sigla válida para sexo: ")

# Sexo ('M' ou 'F')
estadoCivil = input("Informe seu estado civil: ")
while ((estadoCivil != 'S') and (estadoCivil != 'C') and
       (estadoCivil != 'V') and (estadoCivil != 'D')):
    print("Estado civil inválido (digite 'S' ou 'C' ou 'V' ou 'D')")
    estadoCivil = input("Por favor, informe uma sigla válida: ")


if (sexo == 'M'):
    sexo = "Masculino"
else:
    sexo = "Feminino"

if (estadoCivil == 'S'):
    estadoCivil = "Solteiro(a)"
elif (estadoCivil == 'C'):
    estadoCivil = "Casado(a)"
elif (estadoCivil == 'V'):
    estadoCivil = "Viúvo(a)"
elif (estadoCivil == 'D'):
    estadoCivil = "Divorciado(a)"

# Juntando todas as informações
print("O seu nome é: {}".format(nome))
print("Sua idade é: {}".format(idade))
print("Seu salário é: {}".format(salario))
print("Seu sexo é: {}".format(sexo))
print("Seu estado civil é: {}".format(estadoCivil))
print("Fim do programa.")
