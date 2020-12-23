"""
59. Write a Python program to convert height (in feet and inches)
    to centimeters.
"""

print("Input your height: ")
hFeet = int(input("Feet: "))
hInch = int(input("Inches: "))

hInch += hFeet * 12
hCm = round(hInch * 2.54, 1)

print("Your height is: %d cm." % hCm)
