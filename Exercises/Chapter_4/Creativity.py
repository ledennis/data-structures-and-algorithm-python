# C-4.9
def minMax(A, mini=None, maxi=None, length=0):
    if length == 0:
        mini, maxi = A[0], A[0]
    if length == len(A):
        return (mini, maxi)
    else:
        if A[length] > maxi:
            maxi = A[length]
        elif A[length] < mini:
            mini = A[length]
        return minMax(A, mini, maxi, length+1)

# C-4.10
# Describe recursive algo to compute the integer of the base-2 logarithm by using only addition and integer division.
def logarithm(n, log=1):
    if n <= 2:
        return log
    else:
        return logarithm(n//2, log+1)

# C-4.11
def unique3(S, length=0):
    ''' Running time is O(n^2) since each element in S is compared n times. '''
    if length == len(S)-1:
        return unique(S, length)
    else:
        if unique(S, length):
            return unique3(S, length+1)
        else:
            return False

def unique(S, el):
    count = 0
    for items in S:
        if items == S[el]:
            count+=1
    return count == 1

# C-4.12
def product(X, Y, prod=0):
    if X == 0 or Y == 0:
        return 0
    if X == 1:
        return prod + Y
    elif X == -1:
        return prod - Y
    elif X > 1:
        return product(X-1, Y, prod+Y)
    else:
        return product(X+1, Y, prod-Y)

# C-4.13
# N/A

# C-4.14
# Tower of Hanoi, n disks, each with weight to their respective number. Move disks from peg a to c, never placing
# a larger disk on a smaller one. The disks from top to bottom are from smallest to largest.
# 1 - - > - - - > - - - > - - - > - - - > - - - > - - - > - - 1
# 2 - - > 2 - - > - - - > - 1 - > - 1 - > - - - > - - 2 > - - 2
# 3 - - > 3 - 1 > 3 2 1 > 3 2 - > - 2 3 > 1 2 3 > 1 - 3 > - - 3

# 1 - - > - - - > - - - > - - - > - - - > - - - > - - - > - - - > - - - > - - - > - - - > - - - > - - -
# 2 - - > 2 - - > - - - > - - - > - - - > - - - > - - - > 1 - - > 1 - - > - - - > - - - > - 1 - > - 1 -
# 3 - - > 3 - - > 3 - - > 3 1 - > - 1 - > - - 1 > 2 - 1 > 2 - - > 2 - - > 2 - - > - 2 - > - 2 - > - 2 -
# 4 - - > 4 - 1 > 4 2 1 > 4 2 - > 4 2 3 > 4 2 3 > 4 - 3 > 4 - 3 > 4 3 - > 4 3 1 > 4 3 1 > 4 3 - > - 3 4
def towerOfHanoi(n):
    tower = [0] * n
    for i in range(n):
        tower[i] = i
    print('Starting')
    return helperTowerOfHanoi(tower, [], [], n)

def helperTowerOfHanoi(A, B, C, length):
    print(A, B, C)

def move(A, B):
    B.append(A[0])
    B.insert(0, B.pop(B.index(A[0])))
    A.remove(A[0])

def empty(A):
    return len(A) == 0

if __name__ == '__main__':
    # # C-4.9
    # A = [1,2,3,4,5]
    # B = [5,4,3,2,1]
    # C = [-1,-2,-3,-4,-5]
    # D = [-5,4,3,2,-1]
    # print(minMax(A))
    # print(minMax(B))
    # print(minMax(C))
    # print(minMax(D))
    #
    # # C-4.10
    # print(logarithm(2))
    # print(logarithm(4))
    # print(logarithm(8.9))
    # print(logarithm(23.9))
    #
    # # C-4.11
    # A = [1,2,3,4,5]
    # B = [1,2,2,4,5]
    # C = [1,2,2,2,5]
    # D = [-2,2,3,4,-2]
    # F = [0,-1,2,3,8]
    # print(unique3(A))
    # print(unique3(B))
    # print(unique3(C))
    # print(unique3(D))
    # print(unique3(F))
    #
    # # C-4.12
    # print(product(1,5))
    # print(product(5,1))
    # print(product(25,5))
    # print(product(-25,5))
    # print(product(25,-5))
    # print(product(-25,-5))

    # C-4.13
    # print(towerOfHanoi(2))
    # print(towerOfHanoi(3))
    print(towerOfHanoi(4))
