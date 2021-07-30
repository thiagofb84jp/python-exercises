'''
25. Write a Python program to check whether a specified
    value is contained in a group of values
'''


def isGroupMember(groupData, number):
    for value in groupData:
        if (number == value):
            return True
    return False


print(isGroupMember([1, 5, 8, 3], 3))
print(isGroupMember([5, 8, 3], -1))
