'''
36. Write a Python program to add two objects
    if both objects are an integer type.
'''


def addNumbers(x, y):
    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError("Inputs must be integers.")

    return x + y


print(addNumbers(10, 20))
print(addNumbers(3, 5))
print(addNumbers('5', 3))
print(addNumbers(3, 2.0))
