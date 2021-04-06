"""
29. Write a Python program to print out a set
    containing all the colors from color_list_1
    which are not present in color_list_2.
"""

L1 = ["White", "Black", "Red"]
L2 = ["Red", "Green"]

colorList1 = set(L1)
colorList2 = set(L2)

print("Difference between L1 and L2: ", colorList1 - colorList2)
print("Other way to display the difference (L1 - L2): ",
      colorList1.difference(colorList2))
