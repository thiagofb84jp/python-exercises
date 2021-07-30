"""
9. Faça um Programa que peça a temperatura em graus Fahrenheit,
   transforme e mostre a temperatura em graus Celsius.
"""

fahrenheit = 98

celsius = 5 * ((fahrenheit - 32) / 9)

print('{}°F equivale a {:.2f}°C.'.format(fahrenheit, celsius))
