"""
06. Write a Python function to check whether a number
    is in a given range.
"""


def testRange(n):
    if n in range(3, 9):
        print(" %s is in the range " % str(n))
    else:
        print("The number is outside the given range.")


testRange(5)
testRange(2)
testRange(8)
testRange(25)
