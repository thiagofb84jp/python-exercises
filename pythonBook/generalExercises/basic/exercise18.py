"""
18. Write a Python program to calculate the sum of
    three given numbers, if the values are equal then
    return thrice of their sum.
"""


def sumThrice(x, y, z):
    sum = x + y + z

    if x == y == z:
        sum *= 3
    return sum


print(sumThrice(1, 2, 3))
print(sumThrice(3, 3, 3))
