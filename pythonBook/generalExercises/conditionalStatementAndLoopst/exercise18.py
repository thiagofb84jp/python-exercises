"""
18. Write a Python program to print alphabet pattern 'D'.
"""

resultString = ""

for row in range(0, 7):
    for column in range(0, 7):
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
            resultString += "*"
        else:
            resultString += " "
    resultString += "\n"

print(resultString)
