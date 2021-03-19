'''
8. Write a Python function that takes a list of words and returns the
    length of the longest one.
'''


def findLongestWord(wordsList):
    wordLength = []

    for n in wordsList:
        wordLength.append((len(n), n))
    wordLength.sort()

    return wordLength[-1][0], wordLength[-1][1]


result = findLongestWord(["PHP", "Exercises", "Backend"])

print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])
