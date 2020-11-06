# Tipos Numéricos - Parte 2
# Importação de uma biblioteca em Python
from decimal import Decimal, getcontext

print(1.1 + 2.2)
print(Decimal(1) / Decimal(7))

getcontext().prec = 4
print(Decimal(1) / Decimal(7))
print(Decimal.max(Decimal(1), Decimal(7)))
print(dir(Decimal))

print(1.1 + 2.2)
getcontext().prec = 10
print(Decimal(1.1) / Decimal(2.2))
print(dir)
