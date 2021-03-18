"""
5. Write a Python program to calculate surface volume and area of a cylinder.
"""

pi = 22 / 7
height = float(input("Height of cylinder: "))
radian = float(input("Radius of cylinder: "))

volume = pi * radian * radian * height

surfaceArea = ((2 * pi * radian) * height) + ((pi * radian ** 2) * 2)

print("Volume is: {:.2f}".format(volume))
print("Surface Area is: {:.2f}".format(surfaceArea))
