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
