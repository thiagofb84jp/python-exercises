"""
16. Write a Python function to create and print a list
    where the values are square of numbers between 1
    and 30 (both included).
"""


def printValues():
    L = list()

    for i in range(1, 21):
        L.append(i ** 2)

    print(L)


printValues()
