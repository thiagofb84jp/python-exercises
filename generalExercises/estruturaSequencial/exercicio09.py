# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
# em graus Celsius.

fahrenheit = float(input("Temperatura em Fahrenheit(oF): "))

celsius = (5 / 9) * (fahrenheit - 32)

print("Temperatura em Celsius: {:.2f}".format(celsius))
