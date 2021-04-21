'''
8. Write a Python program that prints all the numbers
    from 0 to 6 except 3 and 6.
'''

for e in range(7):
    if (e == 3) or (e == 6):
        continue
    print(e, end=' ')
