# Gerando informação randômica

from random import randint
from datetime import datetime


def genRandoNumber(a, b):
    return randint(a, b)


def genDateTime():
    now = datetime.now()
    return now.day


# print(genRandoNumber(0, 5000))
# genDateTime()

print("SJ", genRandoNumber(0, 5000), genDateTime())

