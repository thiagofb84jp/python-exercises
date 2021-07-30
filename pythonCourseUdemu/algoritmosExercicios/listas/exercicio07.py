"""
07. Write a Python program to remove duplicates from a list.
"""

x = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

duplItems = set()
uniqueItems = []

for i in x:
    if i not in duplItems:
        uniqueItems.append(i)
        duplItems.add(i)

print(duplItems)
