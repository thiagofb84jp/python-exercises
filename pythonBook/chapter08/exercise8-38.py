# Programa 8.39. Módulo soma

from entrada import validaInteiro

L = []
for x in range(10):
    L.append(validaInteiro("Digite um número: ", 0, 20))

print(f"Soma: {sum(L)}")
