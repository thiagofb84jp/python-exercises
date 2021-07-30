'''
26. Write a Python program to create a histogram from a
    given list of integers
'''


def histogram(items):
    for number in items:
        output = ''
        times = number

        while (times > 0):
            output += '*'
            times -= 1

        print(output)


histogram([2, 3, 6, 5, 10, 100])
