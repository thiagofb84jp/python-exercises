'''
23. Write a Python program to get the n (non-negative integer)
    copies of the first 2 characters of a given string. Return
    the n copies of the whole string if the length is less than 2.
'''


def substringCopy(string, number):
    flen = 2

    if (flen > len(string)):
        flen = len(string)
    substring = string[:flen]

    result = ""
    for i in range(number):
        result += substring

    return result


print(substringCopy('abcdef', 2))
print(substringCopy('p', 3))
