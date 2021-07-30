"""
04. Write a Python program to get the smallest number from a list.
"""


def minNumberInList(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i

    return min


print(minNumberInList([1, 2, 8, 0]))
print(minNumberInList([28, 99, 876, 15]))
