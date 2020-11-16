"""
10. Faça um Programa que pergunte em que turno você estuda.
    Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
"""

turno = 'M'.upper()

if turno == 'M':
    print("Bom Dia!")
elif turno == 'V':
    print("Boa Tarde!")
elif turno == 'N':
    print("Boa Noite!")
else:
    print("Valor Inválido!")
