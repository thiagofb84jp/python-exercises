"""
22. Write a Python program to count the number
    4 in a given list.
"""


def listCount(nums):
    count = 0

    for num in nums:
        if num == 4:
            count += 1

    return count


print(listCount([1, 4, 6, 7, 4]))
print(listCount([1, 4, 6, 4, 7, 4]))
