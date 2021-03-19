'''
6. Write a Python program to add 'ing' at the end of a given string
    (length should be at least 3). If the given string already ends
        with 'ing' then add 'ly' instead. If the string length of the
        given string is less than 3, leave it unchanged.
'''


def addString(string):
    length = len(string)

    if length > 2:
        if string[-3:] == 'ing':
            string += 'ly'
        else:
            string += 'ing'

    return string


print(addString('ab'))
print(addString('abc'))
print(addString('string'))
