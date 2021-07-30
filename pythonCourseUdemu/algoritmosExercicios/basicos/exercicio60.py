"""
60.Write a Python program to calculate the hypotenuse of a right
    angled triangle. 
"""

from math import sqrt
print("Input lengths of shorter triangle sides: ")
x = float(input("value one: "))
y = float(input("value two: "))

c = sqrt(x**2 + y**2)

print("The lenght of the hypotenusa is: ", c)
