from random import randint

def punishment():
    randSet = set()
    message = 'I swear I will not spam my friends again.'
    randomMessages = [
    'I swaer I will not spam my friends again.',
    'I swear I wiil not spam my friends again.',
    'I swear I will n0t spam my friends again.',
    'I swear I will not spAm my friends again.',
    'I swear I will not spam mi friends again.',
    'I swear I will not spam my freinds again.',
    'I swear I will not spam my friends agian.',
    'I swear I will not spam my friends gain.',
    ]
    randMessagesGen = randGen(randomMessages)
    for i in range(0, 8):
        randSet.add(randint(0, 100))
    print(randSet)
    for i in range(0, 101):
        if i not in randSet:
            print(i, message)
        else:
            print(i, next(randMessagesGen))

def randGen(list):
    for i in list:
        yield i

punishment()
