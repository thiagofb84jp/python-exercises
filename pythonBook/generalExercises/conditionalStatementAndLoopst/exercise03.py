'''
3. Write a Python program to guess a number between 1 to 9.
'''

import random

targetNumber, guessNumber = random.randint(1, 10), 0
while targetNumber != guessNumber:
    guessNumber = int(
        input('Guess a number between 1 and 10 until you get it right: '))

print("Well guessed!")
