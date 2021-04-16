# Procura uma string


def procuraString(string, lista):
    return string in lista


L = ["AB", "CD", "EF", "FG"]

print(procuraString("AB", L))
print(procuraString("CD", L))
print(procuraString("EF", L))
print(procuraString("XYZ", L))
