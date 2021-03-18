"""
9. Write a Python program to find the smallest multiple of the first n numbers.
    Also, display the factors.
"""


def smalletsMultiple(n):
    if n <= 2:
        return n

    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    print(factors)

    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if a == factors[-1] and i % a == 0:
                return i


print(smalletsMultiple(13))
print(smalletsMultiple(11))
print(smalletsMultiple(2))
print(smalletsMultiple(1))
