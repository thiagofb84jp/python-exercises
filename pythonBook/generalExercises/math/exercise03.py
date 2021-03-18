"""
3. Write a Python program to calculate the area of a trapezoid.
"""

height = float(input("Height of trapezoid: "))
baseOne = float(input("Base one value: "))
baseTwo = float(input("Base two value: "))

area = ((baseOne + baseTwo) / 2) * height

print("Area is: ", area)
