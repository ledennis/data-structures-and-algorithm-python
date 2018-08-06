## R-4.1
Given a sequence S, find max element of n elements recursively.
max = S[n]
Base Case: n == 0
return max
Recursive Step:
if S[n] > max, max = S[n]
Do recursion(n-1)

Runs in O(n) time and has a space of O(n) since each element is gone through once
