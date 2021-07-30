'''
01. Write a Python program to calculate the length of a string.
'''


def stringLength(string):
    count = 0

    for char in string:
        count += 1

    return count


print(stringLength('w3resource.com'))
print(stringLength('Here I am today with you talking about something.'))
