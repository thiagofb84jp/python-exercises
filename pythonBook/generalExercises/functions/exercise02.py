'''
2. Write a Python function to sum all the numbers in a list.
'''


def sum(numbers):
    total = 0

    for x in numbers:
        total += x

    return total


print(sum((8, 2, 3, 0, 7)))
print(sum((10, 20, 30, 40)))
