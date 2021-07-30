# Desafio de Operadores Lógicos

# Os trabalhos
trabalhoTerca = True
trabalhoQuinta = True

"""
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apeans 1: TV 32' + Sorvete
- Nenhum confirmado: Fica em casa + Saudável
"""
tv50 = trabalhoTerca and trabalhoQuinta
sorvete = trabalhoTerca or trabalhoQuinta
tv32 = trabalhoTerca != trabalhoQuinta
maisSaudavel = not sorvete

print("TV 50={} TV 32={} Sorvete={} Saudável={}"
      .format(tv50, tv32, sorvete, maisSaudavel))

print("{1}, {2} = {0}".format(1, False, 'resultado'))
