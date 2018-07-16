from random import *

alphabet = []

def letterCount(fileName):
    """ Creates a dictionary of letters and tracks # of occurences. """

    letterDict={}
    txt = open(fileName)
    letters = txt.read()
    high = 0

    for i in range(97, 123):
        alphabet.append(chr(i))

    for i in range(len(letters)):
        letter = letters[i]
        if letter in alphabet:
            if letter not in letterDict:
                letterDict[letter] = 1
            else:
                letterDict[letter] += 1
                if letterDict[letter] > high:
                    high = letterDict[letter]

    letterChart(letterDict, high)

def letterChart(letterDict, height):
    """ Creates a 26 * height+1 matrix, the additional height is for letters. """

    matrix = [[' ' for x in range(26)] for y in range(height+1)]

    for i in range(len(alphabet)):
        matrix[0][i] = alphabet[i]

    for x in range(len(alphabet)):
        if alphabet[x] in letterDict:
            for i in range(letterDict[alphabet[x]]):
                matrix[i+1][x] = '-'

    writeChart(letterDict, matrix)

def writeChart(letterDict, matrix):
    """ Writes to file by iterating rows of matrix from greatest to least. """

    fileName = 'barGraph.txt'
    fp = open(fileName, 'w')
    for x in range(len(matrix)-1, -1, -1):
        for y in range(len(matrix[0])):
            fp.write(str(matrix[x][y]))
        fp.write('\n')

def generateRandomTxt(fileName, num=100):
    """ Generates a file with random characters from the alphabet. """
    fp = open(fileName, 'w')
    for i in range(num):
        fp.write(chr(randint(97,122)))

if __name__ == '__main__':
    fileName = 'P2_34.txt'
    generateRandomTxt(fileName, 1000)
    letterCount(fileName)
