"""
9. Write a Python function that takes a number
    as a parameter and check the number is prime or not.
"""


def testPrime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False

        return True


print(testPrime(1))
print(testPrime(2))
print(testPrime(5))
print(testPrime(9))
print(testPrime(8))
print(testPrime(33))
