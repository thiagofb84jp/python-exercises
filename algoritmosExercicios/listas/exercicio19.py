'''
19. Write a Python program to get the difference between the two lists.
'''

listOne = [1, 3, 5, 7, 8, 9]
listTwo = [1, 2, 4, 6, 7, 8]

differenceListOneForListTwo = list(set(listOne) - set(listTwo))
differenceListTwoForListOne = list(set(listTwo) - set(listOne))

totalDifference = differenceListOneForListTwo + differenceListTwoForListOne

print(totalDifference)
