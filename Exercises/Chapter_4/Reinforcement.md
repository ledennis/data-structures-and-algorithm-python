## R-4.1
Given a sequence S, find max element of n elements recursively.
max = S[n]
Base Case: n == 0
return max
Recursive Step:
if S[n] > max, max = S[n]
Do recursion(n-1)

Runs in O(n) time and has a space of O(n) since each element is gone through once

## R-4.2
```
def power(x, n):
  if n == 0:
    return 1
  else:
    return x * power(x, n-1)
```
Recursion trace of power(2, 5)
^
return 2 * 16 = 32
|
power(2, 5)
^
return 2 * 8 = 16
|
power(2, 4)
^
return 2 * 4 = 8
|
power(2, 3)
^
return 2 * 2 = 4
|
power(2, 2)
^
return 1 * 2 = 2
|
power(2, 1)
^
return 1
|
power(2, 0)

## R-4.3
```
def power(x, n):
  if n == 0:
    return 1
  else:
    partial = power(x, n//2)
    result = partial * partial
    if n % 2 == 1:
      result *= x
    return result
```
Recursion trace of power(2, 18)
^
return 512 * 512 = 262144
|
power(2, 18)
^
return 16 * 16 * 2 = 512
|
power(2, 9)
^
return 4 * 4 = 16
|
power(2, 4)
^
return 2 * 2 = 4
|
power(2, 2)
^
return 1 * 1 * 2 = 2
|
power(2, 1)
^
return 1
|
power(2, 0)

## R-4.4
```
def reverse(S, starts, stop):
  if start < stop - 1:
    S[start], S[stop-1] = S[stop-1], S[start]
    reverse(S, start+1, stop-1)
```
reverse(S, 0, 5) on S=[4,3,6,2,6]
[6,2,6,3,4] <- end
^
|
[6,3,6,2,4]
^
|
[4,3,6,2,6] <- start

## R-4.5
```
def PuzzleSolve(k, S, U):
  for each e in U do:
    add e to the end of S
    remove e from U
    if k==1 then:
      Test whether S is a configuration that solves the puzzle
      if S solves the puzzle then:
        return "Solution found: " S
    else:
      PuzzleSolve(k-1, S, U)
    Remove e from the end of S
    Add e back to U
```
PuzzleSolve(3, S, U), where S is empty and U={a,b,c,d}

PuzzleSolve(1, S=[d,c], U=[a,b]) = dca, dcb
PuzzleSolve(1, S=[d,b], U=[a,c]) = dba, dbc
PuzzleSolve(1, S=[d,a], U=[b,c]) = dab, dac
PuzzleSolve(2, S=[d], U=[a,b,c])
PuzzleSolve(1, S=[c,d], U=[a,b]) = cda, cdb
PuzzleSolve(1, S=[c,b], U=[a,d]) = cba, cbd
PuzzleSolve(1, S=[c,a], U=[b,d]) = cab, cad
PuzzleSolve(2, S=[c], U=[a,b,d])
PuzzleSolve(1, S=[b,d], U=[a,c]) = bda, bdc
PuzzleSolve(1, S=[b,c], U=[a,d]) = bca, bcd
PuzzleSolve(1, S=[b,a], U=[c,d]) = bac, bad
PuzzleSolve(2, S=[b], U=[a,c,d])
PuzzleSolve(1, S=[a,d], U=[b,c]) = adb, adc
PuzzleSolve(1, S=[a,c], U=[b,d]) = acb, acd
PuzzleSolve(1, S=[a,b], U=[c,d]) = abc, abd
PuzzleSolve(2, S=[a], U=[b,c,d])
PuzzleSolve(3, S, U), S = [], U = [a, b, c, d]

## R-4.6
```
def harmonicNum(k):
  if k == 1:
    return 1
  else:
    return 1/k + harmonicNum(k-1)
```

## R-4.7
```
def stringToDigit(k):
  if int(k) // 10 == 0:
    return int(k)
  else:
    return int(k[0])*(10**(len(k)-1)) + stringToDigit(k[1:])
```

## R-4.8
__Isabel's Algorithm__
```
def sumSequence(A):
  B = [0] * len(A)//2
  B[i] = A[2i] + A[2i+1], for i = 0,1 ... (n/2)-1
  if len(B) == 1:
    return B[0]
  else:
    sumSequence(B)
```
Running time is O(n^2) since there is n/2 summations * n accesses to the array.
