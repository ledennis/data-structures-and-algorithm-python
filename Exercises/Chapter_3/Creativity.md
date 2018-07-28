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
