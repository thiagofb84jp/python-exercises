'''
22. Write a Python program to count the
    number 4 in a given list.
'''


def listCount4(numbers):
    count = 0
    for number in numbers:
        if number == 4:
            count += 1

    return count


print(listCount4([1, 4, 6, 7, 4]))
print(listCount4([1, 4, 6, 4, 7, 4]))
