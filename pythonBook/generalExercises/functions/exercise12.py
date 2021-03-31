"""
12. Write a Python function that checks whether a passed
    string is palindrome or not.
"""


def isPalindrome(string):
    leftPos = 0
    rightPos = len(string) - 1

    while rightPos >= leftPos:
        if not string[leftPos] == string[rightPos]:
            return False

        leftPos += 1
        rightPos -= 1

    return True


print(isPalindrome('aza'))
print(isPalindrome('rato'))
print(isPalindrome('ovo'))
