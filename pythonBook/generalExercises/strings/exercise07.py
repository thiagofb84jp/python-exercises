'''
7. Write a Python program to find the first appearance of the
    substring 'not' and 'poor' from a given string, if 'not'
    follows the 'poor', replace the whole 'not'...'poor' substring
    with 'good'. Return the resulting string.
'''


def notPoor(string):
    sNot = string.find('not')
    sPoor = string.find('poor')

    if (sPoor > sNot) and (sNot > 0) and (sNot > 0):
        string = string.replace(string[sNot:(sPoor + 4)], 'good')
        return string
    else:
        return string


print(notPoor('The lyrics is not that poor!'))
print(notPoor('The lyrics is poor!'))
print(notPoor('The food is not good and poor!'))
