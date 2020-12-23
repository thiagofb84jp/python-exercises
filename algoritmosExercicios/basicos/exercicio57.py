"""
57. Write a program to get execution time (in seconds) for a Python method.
"""

import time


def sumOfNNumbers(number):
    startTime = time.time()
    s = 0

    for i in range(1, n + 1):
        s += i

    endTime = time.time()
    return s, endTime - startTime


n = 5

print("\nTime to sum of 1 to ", n,
      " and required time to calculate is: ", sumOfNNumbers(n))
