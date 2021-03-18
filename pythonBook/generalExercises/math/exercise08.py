"""
8. Write a Python program to calculate the area of a sector.
"""


def sectorArea():
    pi = 22 / 7

    radius = float(input("Radius of Circle: "))
    angle = float(input("Angle meansure: "))

    if angle >= 360:
        print("Angle is not possible")
        return

    surfaceArea = (pi * radius ** 2) * (angle / 360)
    print("Sector Area: {:.2f}".format(surfaceArea))


sectorArea()
