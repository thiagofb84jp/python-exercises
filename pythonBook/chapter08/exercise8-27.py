# Valida o tamanho de uma string


def validaString(string, min, max):
    tamanho = len(string)
    return min <= tamanho <= max


print(validaString("", 1, 5))
print(validaString("ABC", 2, 5))
print(validaString("ABCEFG", 3, 5))
print(validaString("ABCDEFG", 1, 10))
