# 9.12. Gerando números pares e ímpares no mesmo arquivo

def leNumero(arquivo):
    while True:
        numero = arquivo.readline()
        if numero == "":
            return None
        if numero.strip() != "":
            return int(numero)


def escreveNumero(arquivo, n):
    arquivo.write(f"{n}\n")


pares = open("pares.txt", "r")
impares = open("impares.txt", "r")
paresEImpares = open("paresEImpares.txt", "w")
nPar = leNumero(pares)
nImpar = leNumero(impares)

while True:
    if nPar is None and nImpar is None:
        break
    if nPar is not None and (nImpar is None or nPar <= nImpar):
        escreveNumero(paresEImpares, nPar)
        nPar = leNumero(pares)
    if nImpar is not None and (nPar is None or nImpar <= nPar):
        escreveNumero(paresEImpares, nImpar)
        nImpar = leNumero(impares)


paresEImpares.close()
pares.close()
impares.close()
