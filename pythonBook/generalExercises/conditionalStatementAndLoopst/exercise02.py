'''
2. Write a Python program to convert temperatures to and from celsius,
    fahrenheit.
'''

temp = input("Input the temperature you like to convert: ")
degree = int(temp[:-1])
iConvention = temp[-1]

if iConvention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    oConvention = "Fahrenheit"
elif iConvention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    oConvention = "Celsius"
else:
    print("Input proper convention.")
    quit()
print("The temperature in ", oConvention, " is ", result, "degrees.")
