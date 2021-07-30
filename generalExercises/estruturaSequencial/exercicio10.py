# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em 
# graus Fahrenheit.

celsius = float(input("Temperatura em Celsius(oC): "))

fahrenheit = 9 * celsius / 5 + 32

print("Temperatura em Fahrenheit: {:.2f}".format(fahrenheit))
