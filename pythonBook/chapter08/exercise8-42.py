# Trabalhando com tipos em Python

import types


def dizOTipo(a):
    if isinstance(a, str):
        return "String"
    elif isinstance(a, list):
        return "Lista"
    elif isinstance(a, dict):
        return "Dicionário"
    elif isinstance(a, int):
        return "Número Inteiro"
    elif isinstance(a, float):
        return "Número Decimal"
    elif isinstance(a, types.FunctionType):
        return "Função"
    elif isinstance(a, types.BuiltinFunctionType):
        return "Função Interna"
    else:
        return str(type(a))


print(dizOTipo(10))
print(dizOTipo(10.5))
print(dizOTipo("Alô"))
print(dizOTipo([1, 2, 3]))
print(dizOTipo({"a": 1, "b": 50}))
print(dizOTipo(print))
print(dizOTipo(None))
print()

L = [2, "Alô", ["!"], {"a": 1, "b": 2}]
for e in L:
    print(type(e))
