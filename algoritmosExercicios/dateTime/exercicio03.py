'''
03. Write a Python program to convert a string to datetime.
'''

from datetime import datetime

dateObject = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')

print(dateObject)
