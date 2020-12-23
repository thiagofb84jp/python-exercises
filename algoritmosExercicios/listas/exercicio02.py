"""
2. Write a Python program to multiplies all the items in a list.
"""


def multiplyList(items):
    total = 1

    for i in items:
        total *= i

    return total


print(multiplyList([1, 2, -8]))
