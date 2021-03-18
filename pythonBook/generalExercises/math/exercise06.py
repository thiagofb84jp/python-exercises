"""
6. Write a Python program to calculate surface volume and area of a sphere.
"""

pi = 22 / 7

radian = float(input("Radius of sphere: "))
surfaceArea = 4 * pi * radian ** 2
volume = (4 / 3) * (pi * radian ** 3)

print("Surface Area is: {:.4f}".format(surfaceArea))
print("Volume is: {:.4f}".format(volume))
