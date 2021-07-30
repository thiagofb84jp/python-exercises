'''
30. Write a Python program that will accept
    the base and height of a triangle and compute
    the area.
'''

base = float(input("Input the base: "))
height = float(input("Input the height: "))

area = (base * height) / 2

print("Area = {:.2f}".format(area))
