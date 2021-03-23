"""
4.13. Calculadora
"""

a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
operacao = input("Digite a operação a realizar (+, -, * ou /): ")

if operacao == "+":
    resultado = a + b
elif operacao == "-":
    resultado = a - b
elif operacao == "*":
    resultado = a * b
elif operacao == "/":
    resultado = a / b
else:
    print("Operação inválida!")
    resultado = 0

print(f"Resultado: {resultado:0.2f}")
