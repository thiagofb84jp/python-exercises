'''
4. Write a Python program to reverse a string.
'''

def stringReverse(string):
    reverseString = ''
    index = len(string)

    while index > 0:
        reverseString += string[index - 1]
        index -= 1

    return reverseString


print(stringReverse('1234abcd'))
print(stringReverse('Joana Has Been Deployed on The Project'))
