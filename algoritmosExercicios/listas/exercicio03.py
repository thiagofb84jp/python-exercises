"""
03. Write a Python program to get the largest number from a list.
"""


def maxNumberInList(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i

    return max


print(maxNumberInList([1, 2, -8, 0]))
print(maxNumberInList([28, 99, -876, 15]))
