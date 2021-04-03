"""
17. Write a Python program to test whether a number is within
    100 of 1000 or 2000. 
"""


def nearThousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))


print(nearThousand(1000))
print(nearThousand(900))
print(nearThousand(800))
print(nearThousand(2200))
