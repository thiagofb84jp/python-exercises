"""
10. Write a Python program to find the list of words that are longer
    than n from a given list of words.
"""


def longWords(n, str):
    wordLeng = []
    txt = str.split(" ")

    for i in txt:
        if len(i) > n:
            wordLeng.append(i)

    return wordLeng


print(longWords(3, "The quick brown fox jumps over the lazy dog and moving around the corner."))
