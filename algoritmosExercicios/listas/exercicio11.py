"""
11. Write a Python function that takes two lists and returns True
    if they have at least one common member. 
"""


def commonData(list1, list2):
    result = False

    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result


print(commonData([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(commonData([1, 2, 3, 4, 5], [6, 7, 8, 9]))
print(commonData([1, 2, 3, 4, 5], [1, 7, 8, 9]))
print(commonData([1, 2, 3, 4, 5], [10, 7, 8, 9, 8]))
