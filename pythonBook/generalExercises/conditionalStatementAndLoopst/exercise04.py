'''
4. Write a Python program to construct the following pattern,
    using a nested for loop.
'''

n = 100

for e in range(n):
    for f in range(e):
        print("*", end="")
    print("")

for e in range(n, 0, -1):
    for f in range(e):
        print("*", end="")
    print("")
