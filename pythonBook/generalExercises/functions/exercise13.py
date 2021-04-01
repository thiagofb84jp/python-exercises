"""
13. Write a Python function that that prints out the first
    n rows of Pascal's triangle.
"""


def pascalTriangle(n):
    trow = [1]
    y = [0]

    for x in range(max(n, 0)):
        print(trow)
        trow = [l + r for l, r in zip(trow + y, y + trow)]

    return n >= 1


pascalTriangle(6)
