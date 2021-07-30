'''
52. Write a Python program to print to stderr.
'''

from __future__ import print_function
import sys


def ePrint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


ePrint("abc", "efg", "xyz", sep="--")
