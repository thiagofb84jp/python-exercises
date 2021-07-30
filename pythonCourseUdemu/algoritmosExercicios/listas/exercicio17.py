'''
17. Write a Python program to generate and print a
    list except for the first 5 elements, where the
    values are square of numbers between 1 and 30 (both included).
'''


def printValues():
    listValues = list()

    for i in range(1, 21):
        listValues.append(i**2)

    print(listValues[:5])


printValues()
