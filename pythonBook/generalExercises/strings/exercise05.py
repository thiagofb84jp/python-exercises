'''
5. Write a Python program to get a single string
    from two given strings, separated by a space
    and swap the first two characters of each string.
'''


def charsMixUp(a, b):
    newA = b[:2] + a[2:]
    newB = a[:2] + b[2:]

    return newA + ' ' + newB


print(charsMixUp('abc', 'xyz'))
