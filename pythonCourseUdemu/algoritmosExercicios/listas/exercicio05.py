"""
05. Write a Python program to count the number of strings where
    the string length is 2 or more and the first and last character
    are same from a given list of strings.
"""


def matchWords(words):
    ctr = 0

    for word in words:
        if (len(word) > 1) and (word[0] == word[-1]):
            ctr += 1

    return ctr


print(matchWords(['abc', 'xyz', 'aba', '1221']))
print(matchWords(['amanda', 'alicia', 'amanza', 'suzete']))
