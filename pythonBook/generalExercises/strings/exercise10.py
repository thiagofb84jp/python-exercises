'''
10. Write a Python program to change a given string
    to a new string where the first and last chars have
    been exchanged.
'''


def changeString(string):
    return string[-1:] + string[1:-1] + string[:1]


print(changeString('abcd'))
print(changeString('12345'))
print(changeString('Joana'))
