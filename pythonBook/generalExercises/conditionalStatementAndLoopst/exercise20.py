"""
20. Write a Python program to print alphabet pattern 'L'.
"""

resultString = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or (row == 6 and column != 0 and column < 6)):
            resultString += "*"
        else:
            resultString += " "
    resultString += "\n"

print(resultString)
