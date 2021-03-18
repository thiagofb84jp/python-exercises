"""
10. Write a Python program to calculate the discriminant value.
"""


def discriminant():
    xValue = float(input("The 'x' value: "))
    yValue = float(input("The 'y' value: "))
    zValue = float(input("The 'z' value: "))

    discriminant = (yValue ** 2) - (4 * xValue * zValue)

    if discriminant > 0:
        print("Two soluctions. Discriminant value is: ", discriminant)
    elif discriminant == 0:
        print("One soluction. Discriminant value is: ", discriminant)
    elif discriminant < 0:
        print("No Real soluction. Discriminant value is: ", discriminant)


discriminant()
