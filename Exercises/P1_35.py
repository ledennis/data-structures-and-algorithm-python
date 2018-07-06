from random import *

def bDayParadox(n):
    randSet = set()
    for i in range(0, n):
        rand = randint(1, 365)
        if rand not in randSet:
            randSet.add(i)
        else:
            return True
    return False

for i in range(5, 101, 5):
    print(i, bDayParadox(i))
