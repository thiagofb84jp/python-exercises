'''
9. Write a Python program to remove the nth index character from
    a nonempty string.
'''


def removeChar(string, n):
    firstPart = string[:n]
    lastPart = string[n + 1:]

    return firstPart + lastPart


print(removeChar('Python', 0))
print(removeChar('Python', 3))
print(removeChar('Python', 5))
