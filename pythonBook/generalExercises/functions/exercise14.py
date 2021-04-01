"""
14. Write a Python function to check whether a
    string is a pangram or not.
"""

import string


def isPangram(str1, alfabet=string.ascii_lowercase):
    alphaset = set(alfabet)

    return alphaset <= set(str1.lower())


print(isPangram('The quick brown fox jumps over the lazy dog.'))
print(isPangram('Here comes to eternity.'))
