"""
17. Write a Python program to make a chain of
    function decorators (bold, italic, underline etc.).
"""


def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "<b>"
    return wrapped


def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "<i>"
    return wrapped


def makeUnderline(fn):
    def wrapped():
        return "<u>" + fn() + "<u>"
    return wrapped


@makeBold
@makeItalic
@makeUnderline
def hello():
    return "Hello World"


print(hello())
