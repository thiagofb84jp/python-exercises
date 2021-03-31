"""
11. Write a Python function to check whether a number is
    perfect or not.
"""


def perfectNumber(N):
    sum = 0

    for x in range(1, N):
        if N % x == 0:
            sum += x

    return sum == N


print(perfectNumber(6))
print(perfectNumber(2))
