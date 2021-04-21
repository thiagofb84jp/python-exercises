'''
1. Write a Python program to find those numbers which are divisible
    by 7 and multiple of 5, between 1500 and 2700 (both included).
'''

L = []

for e in range(1500, 2701):
    if (e % 7 == 0) and (e % 5 == 0):
        L.append(e)

print(L)
