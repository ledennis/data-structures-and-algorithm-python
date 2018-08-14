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

if __name__ == '__main__':
    # C-4.9
    A = [1,2,3,4,5]
    B = [5,4,3,2,1]
    C = [-1,-2,-3,-4,-5]
    D = [-5,4,3,2,-1]
    print(minMax(A))
    print(minMax(B))
    print(minMax(C))
    print(minMax(D))

    # C-4.10
    print(logarithm(2))
    print(logarithm(4))
    print(logarithm(8.9))
    print(logarithm(23.9))

    # C-4.11
    A = [1,2,3,4,5]
    B = [1,2,2,4,5]
    C = [1,2,2,2,5]
    D = [-2,2,3,4,-2]
    F = [0,-1,2,3,8]
    print(unique3(A))
    print(unique3(B))
    print(unique3(C))
    print(unique3(D))
    print(unique3(F))
