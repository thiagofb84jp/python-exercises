"""
11. Write a Python program which takes two digits m (row)
    and n (column) as input and generates a two-dimensional array.
"""

rowNum = int(input("Input number of rows: "))
colNum = int(input("Input the number of columns: "))
multiList = [[0 for col in range(colNum)] for row in range(rowNum)]

for row in range(rowNum):
    for col in range(colNum):
        multiList[row][col] = row * col

print(multiList)
