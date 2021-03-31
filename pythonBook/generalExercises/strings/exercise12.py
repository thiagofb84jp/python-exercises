"""
12. Write a Python program to count the
    occurrences of each word in a given sentence.
"""


def wordCount(string):
    counts = dict()
    words = string.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


print(wordCount('the quick brown fox jumps over the lazy dog.'))
print(wordCount('Jonathan said that she doesnt love him anymore.'))
print(wordCount('current word with current works'))
