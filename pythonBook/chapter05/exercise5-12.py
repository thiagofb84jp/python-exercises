'''
5.12. Interropendo a repetição
'''

s = 0

while True:
    v = int(input("Digite um número a somar (ou 0 (zero) para sair: "))
    if v == 0:
        break
    s += v

print(f"Soma total: {s}")
