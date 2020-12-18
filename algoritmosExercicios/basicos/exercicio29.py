'''
29. Write a Python program to print out a set
    containing all the colors from color_list_1
    which are not present in color_list_2.
'''

colorListOne = set(["White", "Black", "Red"])
colorListTwo = set(["Red", "Green"])

print(colorListOne.difference(colorListTwo))
