"""
15. A série de Fibonacci é formada pela seqüência
    1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz
    de gerar a série até o n−ésimo termo.
"""

ultimo = 1
penultimo = 1

print(ultimo)
print(penultimo)

for i in range(12):
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    i += 1
    print(termo)
