## C-3.35
Assuming it is possible to sort n numbers in O(nlogn), solve 3-set disjointness in O(nlogn) time
3 sets, A, B, C
For n elements in A, use divide and conquer to search through B and C
Search takes logn time, and is done twice for each element in A
Running time is O(2nlogn) which is O(nlogn)

## C-3.36
Efficient algorithm for finding ten largest elements in sequence of size n.
Sort n using quicksort, which takes up to O(nlogn) time
Return last ten elements
Running time is O(nlogn)

## C-3.37
Example of positive function f(n) such that f(n) is neither O(n) nor bigOmega(n)
O(n): f(n) <= cf(n)
bOmega(n): f(n) >= cf(n)
Neither: f(n) = n^2 when n is even, therefore breaks O(n) since f(n) = n^2 > O(n)
         f(n) = 0 when n is odd, therefore breaks bigOmega(n) since f(n) = 0 < O(n)

## C-3.38
Show that summation of i=1 to n of i^2 is O(n^3)
Since there are n elements, i to n, and n^2 operation for each n, this is O(n^3)

## C-3.39
Show that summation of i=1 to n of i/2^i is less than 2
Since 1 / 2 = .5, as n approaches infinity, the summation approximates to 1, which is less than 2

## C-3.40
log base b f(n) is bTheta(logf(n)) if b > 1 is a constant
Prove logbf(n) is O(logf(n)) and bOmega(logf(n))
Assuming logf(n) is log base 2, then logbf(n) where b = 1, is O(logf(n))
Assuming logf(n) is log base 2, then logbf(n) where b = 3, is bOmega(logf(n))
Therefore logbf(n) is bTheta(logf(n))

## C-3.41
Find min and max of n numbers using 3n/2 comparisons.
First compare the first two numbers of n to determine min and max.
Afterwards, use divide and conquer to find min and max of both sides.
For each n, there is a comparison to the min, max, and possibly another comparison to min or max respectively.
Since it is divide and conquer, each element will only be compared to n/2 elements.
Three comparisons for each n and on n/2 elements equates to 3n/2 comparisons.
Also, since the first two elements are only compared once, there are 3n/2 - 2 comparisons.

## C-3.42
Bob has 1 to n friends and each friend is allowed to visit i times, which could be different from others.
Counter C that keeps track of the total number of visits to the site. Minimum value of C to know that
a friend has reached his/her max.
Minimum value of C is (sum of i - 1) + 1.
The argument is that each friend can have up to i - 1 visit without reaching i number of visits, afterwards, if
one there is one more visit, we know that one friend has reached his/her limit.

## C-3.43
Draw Proposition 3.3, for when n is odd
For any integer n >= 1, we have:
1 + 2 + 3 + ... + (n-2) + (n-1) + n = n(n+1)/2 operations
Can't draw on her but should be similar to Figure 3.3 (b)
A rectangle with base n/2 and up to n+1 height? (Unsure)
 
