'''
27. Write a Python program to concatenate all elements in a list
    into a string and return it.
'''


def concatenateListData(list):
    result = ''

    for element in list:
        result += str(element)

    return result


print(concatenateListData([1, 5, 12, 2, 999]))
