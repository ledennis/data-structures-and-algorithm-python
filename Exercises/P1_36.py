from random import *

def countWords(fileName):
    wordDict = {}
    fp = open(fileName)
    for line in fp:
        word = fp.readline()
        word = word.strip('\n')
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] = wordDict[word] + 1
    print(wordDict)


def writeWords(fileName):
    fp = open(fileName, 'w')
    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

    for i in range(0, 100):
        fp.write(words[randint(0,9)] + '\n')

writeWords('P1_36_words.txt')
countWords('P1_36_words.txt')
