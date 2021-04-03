"""
23. Write a Python program to get the n
    (non-negative integer) copies of the
    first 2 characters of a given string. Return
    the n copies of the whole string if the length
    is less than 2.
"""


def substringCopy(string, n):
    fLen = 2

    if fLen > len(string):
        fLen = len(string)
    substring = string[:fLen]

    result = ""

    for i in range(n):
        result += substring

    return result


print(substringCopy('abcdef', 2))
print(substringCopy('p', 3))
