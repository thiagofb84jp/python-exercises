'''
35. Write a Python program which will return true
    if the two given integer values are equal or their
    sum or difference is 5.
'''


def testNumbers5(x, y):
    if ((x == y) or (abs(x - y) == 5 or (x + y) == 5)):
        return True
    else:
        return False


print(testNumbers5(7, 2))
print(testNumbers5(3, 2))
print(testNumbers5(2, 2))
print(testNumbers5(10, 11))
