"""
8. Write a Python function that takes a list and returns
    a new list with unique elements of the first list.
"""


def uniqueList(l):
    x = []

    for a in l:
        if a not in x:
            x.append(a)

    return x


print(uniqueList([1, 2, 3, 3, 3, 3, 4, 5]))
print(uniqueList([1, 2, 25, 28, 7, 28, 3, 1, 29, 22, 23, 22, 23, 22, 23, 22, 56, 66]))
