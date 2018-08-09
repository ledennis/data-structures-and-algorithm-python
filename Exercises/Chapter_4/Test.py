import time

def stringToDigit(k):
  if int(k) // 10 == 0:
    return int(k)
  else:
    return int(k[0])*(10**(len(k)-1)) + stringToDigit(k[1:])

def sumSequenceRecursive(A):
    B = [0] * (len(A)//2)
    for i in range(0,(len(A)//2)):
        B[i] = A[2*i] + A[2*i+1]
    if len(B) == 1:
        return B[0]
    else:
        return sumSequenceRecursive(B)

def sumSequenceIterative(A):
    summ = 0
    for i in A:
        summ += i
    return summ

if __name__ == '__main__':
    # print(stringToDigit('199'))
    # print(stringToDigit('2100'))
    # print(stringToDigit('0'))

    twoPow = 2**20
    A = [0] * twoPow
    for i in range(0, twoPow):
        A[i] = i
    start = time.time()
    sumSequenceRecursive(A)
    end = time.time()
    print(end - start)

    start = time.time()
    sumSequenceIterative(A)
    end = time.time()
    print(end - start)
