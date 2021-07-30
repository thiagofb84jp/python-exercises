"""
14. Write a Python program to calculate number of days
    between two dates. 
"""

from datetime import date

firstDate = date(2020, 12, 17)
lastDate = date(2020, 12, 25)

delta = lastDate - firstDate

print(delta.days)
