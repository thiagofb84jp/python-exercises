"""
16. Write a Python program to get the difference between
    a given number and 17, if the number is greater than 17
    return double the absolute difference.
"""


def difference(number):
    if (number <= 17):
        return 17 - number
    else:
        return (number - 17) * 2


print(difference(22))
print(difference(14))
