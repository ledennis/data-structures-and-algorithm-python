def permutateBruteForce():
    letters = ['c', 'a', 't', 'd', 'o', 'g']
    permutateBruteForceHelper(letters, '')


def permutateBruteForceHelper(letters, string):
    if len(letters) == 1:
        print(string + letters[0])
    for i in letters:
        nextLetters = [] + letters
        nextLetters.remove(i)
        permutateBruteForceHelper(nextLetters, string + i)

permutateBruteForce()
