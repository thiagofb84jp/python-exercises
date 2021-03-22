"""
3.9. Calcular quantidade de dias, horas, minutos e segundos do usuário.
"""

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

totalEmSegundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos

print(f"Convertido em segundos é igual a {totalEmSegundos} segundos.")
