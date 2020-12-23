'''
08. Write a Python program to convert the date to datetime
    (midnight of the date).
'''

from datetime import date
from datetime import datetime

today = date.today()

print(datetime.combine(today, datetime.min.time()))
