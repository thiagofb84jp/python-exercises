"""
24. Write a Python program to test whether a passed
    letter is a vowel or not.
"""


def isVowel(char):
    allVowels = 'aeiou'

    return char in allVowels


print(isVowel('c'))
print(isVowel('e'))
