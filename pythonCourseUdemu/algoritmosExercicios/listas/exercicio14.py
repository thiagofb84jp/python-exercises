"""
14. Write a Python program to print the numbers of a specified list
    after removing even numbers from it.
"""

number = [7, 8, 120, 25, 44, 20, 27]
number = [x for x in number if x % 2 != 0]

print(number)
