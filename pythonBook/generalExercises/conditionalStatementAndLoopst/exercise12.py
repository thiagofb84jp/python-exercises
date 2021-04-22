"""
12. Write a Python program that accepts a sequence of
    lines (blank line to terminate) as input and prints
    the lines as output (all characters in lower case).
"""

lines = []

while True:
    L = input()
    if L:
        lines.append(L.upper())
    else:
        break


for L in lines:
    print(L)
