'''
39. Write a Python program to compute the future value
    of a specified principal amount, rate of interest,
    and a number of years
'''

amt = 10000
int = 3.5
years = 7

futureValue = amt * ((1 + (0.01 * int)) ** years)
print(round(futureValue, 2))
