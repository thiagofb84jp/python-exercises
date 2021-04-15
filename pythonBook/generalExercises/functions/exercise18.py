"""
18. Write a Python program to execute a string containing
    Python code.
"""

myCode = 'print("Hello World")'
code = """
def multiply(x, y):
    return x * y

print('Multiply of 2 and 3 is: ', multiply(2, 3))
"""

exec(myCode)
exec(code)
