"""
20. Write a Python program to get a string which is n (non-negative integer)
    copies of a given string.
"""


def largerString(str, number):
    result = ""

    for i in range(number):
        result = result + str

    return result


print(largerString('abc', 2))
print(largerString('.py', 3))
