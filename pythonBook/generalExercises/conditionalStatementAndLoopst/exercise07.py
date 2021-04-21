'''
7. Write a Python program that prints each item and its
    corresponding type from the following list.
'''

dataList = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
            {"class": "V", "section": "A"}, 'k']

for e in dataList:
    print("Type of ", e, " is ", type(e))
