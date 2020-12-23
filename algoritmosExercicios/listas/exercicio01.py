"""
01. Write a Python program to sum all the items in a list.
"""


def sumList(items):
    sumNumbers = 0

    for x in items:
        sumNumbers += x

    return sumNumbers


print(sumList([1, 2, -8]))
