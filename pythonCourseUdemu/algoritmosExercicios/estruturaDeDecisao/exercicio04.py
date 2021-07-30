"""
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = "w"

if ((letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o')
        or (letra == 'u')):
    print("A letra '{}' é uma vogal".format(letra))
else:
    print("A letra '{}' é uma consoante".format(letra))
