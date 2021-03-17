'''
7. Write a Python program to accept a filename
    from the user and print the extension of that.
'''

fileName = input("Input the file name: ")
fileExtension = fileName.split(".")

print("The extension of the file is: " + repr(fileExtension[-1]))
