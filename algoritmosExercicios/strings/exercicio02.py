'''
02. Write a Python program to count the number of characters
    (character frequency) in a string.
'''


def charFrequency(string):
    dict = {}

    for i in string:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1

    return dict


print(charFrequency('google.com'))
print(charFrequency('Turtle key is near to you'))
