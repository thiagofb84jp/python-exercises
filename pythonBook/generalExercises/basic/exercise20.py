"""
20. Write a Python program to get a string
    which is n (non-negative integer) copies
    of a given string.
"""


def largerString(string, n):
    result = ""

    for i in range(n):
        result += string

    return result


print(largerString('abc', 2))
print(largerString('.py', 5))
