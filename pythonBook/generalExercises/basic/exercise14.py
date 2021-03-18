"""
14. Write a Python program to calculate number of days between two dates.
"""

from datetime import date

firstDate = date(2014, 7, 2)
lastDate = date(2014, 7, 11)

delta = lastDate - firstDate

print(delta)
