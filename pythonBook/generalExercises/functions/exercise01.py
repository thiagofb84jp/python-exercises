'''
1. Write a Python function to find the Max of three numbers.
'''


def maxOfThree(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > x) and (y > z):
        return y
    elif (z > x) and (z > y):
        return z


print(maxOfThree(50, 20, 30))
print(maxOfThree(44, 75, 15))
print(maxOfThree(25, 35, 105))
