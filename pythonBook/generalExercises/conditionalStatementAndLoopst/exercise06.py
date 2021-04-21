'''
6. Write a Python program to count the number of even and
    odd numbers from a series of numbers.
'''

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
countOdd = 0
countEven = 0

for x in numbers:
    if not x % 2:
        countEven += 1
    else:
        countOdd += 1

print("Number of even numbers: ", countEven)
print("Number of odd numbers: ", countOdd)
