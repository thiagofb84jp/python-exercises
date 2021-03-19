'''
3. Write a Python program to get a string made of the first 2
    and the last 2 chars from a given a string. If the string
    length is less than 2, return instead of the empty string.
'''


def stringBothEnds(string):
    if len(string) < 2:
        return ''

    return string[0:2] + " " + string[-2:]


print(stringBothEnds("w3resource"))
print(stringBothEnds("w3"))
print(stringBothEnds("José da Silva Santos Vasconcelos Lima"))
