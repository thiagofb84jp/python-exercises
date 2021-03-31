"""
10. Write a Python program to print
    the even numbers from a given list.
"""


def isEvenNumber(L):
    enum = []

    for n in L:
        if n % 2 == 0:
            enum.append(n)

    return enum


print(isEvenNumber([1, 2, 3, 4, 5, 6, 7, 8, 9]))
