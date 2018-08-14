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
