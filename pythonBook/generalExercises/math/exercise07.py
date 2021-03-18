"""
7. Write a Python program to calculate arc length of an angle.
"""


def arcLength():
    pi = 22 / 7
    diameter = float(input("Diameter of circle: "))
    angle = float(input("Angle meansure: "))

    if angle >= 360:
        print("Angle is not possible.")
        return

    arcLength = (pi * diameter) * (angle / 360)
    print("Arc Length is: {:.2f}".format(arcLength))


arcLength()
