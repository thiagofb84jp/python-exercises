"""
8. Write a Python program to check a list is empty or not.
"""


def isEmpty(items):
    if not items:
        print("List is empty.")
    else:
        print("List is not empty.")


l = []
m = [10, 20, 30, 40, 50]

print(isEmpty(l))
print(isEmpty(m))
