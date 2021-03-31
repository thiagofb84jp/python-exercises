"""
15. Write a Python function to create the HTML string
    with tags around the word(s).
"""


def addTags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag)


print(addTags('i', 'Python'))
print(addTags('b', 'Python Tutorial'))
