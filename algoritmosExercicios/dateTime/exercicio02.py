'''
02. Write a Python program to determine whether a given year is a leap year.
'''


def leapYear(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False


print(leapYear(1900))
print(leapYear(2004))
print(leapYear(2020))
print(leapYear(2018))
