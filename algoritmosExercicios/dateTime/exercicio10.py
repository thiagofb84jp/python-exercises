'''
10. Write a Python program to add 5 seconds with the current time.
'''

import datetime

x = datetime.datetime.now()
y = x + datetime.timedelta(0, 5)

print(x.time())
print(y.time())
