"""
12. Write a Python program to print a specified list after
    removing the 0th, 4th and 5th elements.
"""

color = ['Grey', 'Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Blue']
color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]

print(color)
