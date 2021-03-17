'''
4. Write a Python program which accepts the radius
    of a circle from the user and compute the area.
'''

from math import pi

radius = float(input("Input the radius of the circle: "))
area = pi * radius ** 2

print("The area of the circle with radius: {} is {:.2f}".format(radius, area))
