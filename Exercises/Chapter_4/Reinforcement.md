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
