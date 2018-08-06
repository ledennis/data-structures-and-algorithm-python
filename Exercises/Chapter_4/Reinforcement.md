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
