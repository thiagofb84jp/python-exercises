"""
11. Write a Python program to remove the characters
    which have odd index values of a given string.
"""


def oddValuesString(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i]

    return result


print(oddValuesString('abcdef'))
print(oddValuesString('python'))
print(oddValuesString('thiago ferreira barbosa'))
