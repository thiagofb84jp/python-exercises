"""
22. Write a Python program to print alphabet pattern 'M'.
"""

resultString = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):
            resultString += "*"
        else:
            resultString += " "
    resultString += "\n"

print(resultString)
