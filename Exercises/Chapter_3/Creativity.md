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

## C-3.44
No efficient algorithm for factoring a large prime number
r = p * q, where r is a number, q is a key/large prime number, and p is the secret message/large prime number
```
for p in range(2,r):
  if r % p == 0:
    return 'The secret message is p!'
```
(a). Worst case to decipher secret message p if the transmitted message r has 100 bits,
where one division takes 1 microsecond?
Each number is represented in 2^n bits. For the worst case, we assume that p and q are the same length, since we can
find q first if q < p, or p first if p < q in length. We can say that p is m/2 length, where m is the size of r.
Therefore the running time is O(2^(m/2)) to find p.
Assuming m = 80, it would take 10^-6 * 2^(50 / 2) ~= 1099511 seconds ~= 12.7 days
(b). Number of bits in r is log_base2_ofr
Since m is the size of r, 2^(log_base2_ofr/2) = 2^(4(log_base2_ofr)/8) = 2^(4n)
and there are O(n) operations, running time is O(n2^(4n))

## C-3.45
Since numbers are unique and are in range [0, n-1], that means that any number > n-1 is not in S.
Running time is O(n), since there can be up to n comparisons against n-1.

## C-3.46
Base case: One sheep is the color of itself.
Al states that if one sheep is taken out, the remaining n-1 sheep are the same color by induction. This is false
since if the base case builds on itself, it only implies that each sheep is their own color, not that they are the
same color.

## C-3.47
Base case n=0
There are 0 intersection points
Induction Step:
Assuming no two lines are parallel and no three meet in the same point. Suppose we have n + 1 lines then, removing one
would have n^2 intersection points. That means that the line that we removed must intersect all other n lines, since
it is not parallel to any lines and no three lines can meet at the same point. Meaning we added n intersection points.
n + 1 = n^2 + n intersection points, which is still n^2, so by induction, there are Theta(n^2) points.
