# 9.4. Parâmetros na linha de comando

import sys

print(f"Número de parâmetros: {len(sys.argv)}")

for n, p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")
