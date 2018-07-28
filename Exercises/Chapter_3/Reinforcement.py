# R-3.1
# 8n < 4nlogn < 2n^2 < n^3 < 2^n
# Linear < nlogn < quadratic < cubic < exponential

# R-3.2
# A = 8nlogn, B = 2n^2, n >= n0
# n0 = 16, A = 8 * 16 * 4 = 1028, B = 2 * 16 * 16 = 1028

# R-3.3
# A = 40n^2, B = 2n^3, n >= n0
# n = 20, A = 40 * 20 * 20 = 16000, B = 2 * 20 * 20 * 20 = 16000

# R-3.4
# f(n) = n
# A linear function will grow linearly on either a log-log scale or a standard scale.


# R-3.5
# Since log-log scales at an exponential base and c is the exponent of n^c, n^c will grow at a slope of c on a log-log scale.

# R-3.6
# Sum of all even numbers between 0 to 2n where n is a positive integer
# Sum(2k) for when k = 1 .. 2n
# 2 + 4 + 6 ... + 2n
# 2(1 + 2 + 3 ... n)
# n(n+1)

# R-3.7
# (a) The running time of algorithm A is always O(f(n))
# (b) In the worst case, the running time of algorithm A is O(f(n))
# a implies b since A is always O(f(n)), which means that in the worst case, the running time is O(f(n)).

# R-3.8
# 2^10 < 2^logn == 4n == 3n + 100logn < 4nlogn + 2n == nlogn < n^2 + 10n < n^3 < 2^n

# R-3.9
# if d(n) = O(f(n)), then ad(n) is O(f(n)) for any constant a > 0
# since O(f(n)) is for asymptoptic growth to infinity, any positive coefficient to d(n) will be neglible as the function approaches infinity, so ad(n) is O(f(n)).

# R-3.10
# if d(n) = O(f(n)) and e(n) is O(g(n)), then d(n)e(n) is O(f(n)g(n))
# Rule of productivity, O(f(n)) * O(g(n)) = O(f(n)g(n))

# R-3.11
# if d(n) = O(f(n)) and e(n) is O(g(n)), then d(n) + e(n) is O(f(n) + g(n))
# if O(f(n) + g(n)), then the bigger asymptoptic growth determines big Oh

# R-3.12
# if d(n) = O(f(n)) and e(n) is O(g(n)), then d(n) - e(n) is not necessarily O(f(n) - g(n))
# If f(n) < g(n), then the big Oh is negative, which means that big Oh grows smaller as n increases, which can not be true.

# R-3.13
# if d(n) = O(f(n)) and f(n) is O(g(n)), then d(n) is O(g(n))
# since d(n) <= cf(n) and f(n) <= cg(n) where c is a positive integer, d(n) <= g(n), which means d(n) is O(g(n)).

# R-3.14
# O(max{f(n), g(n)}) = O(f(n) + g(n))
# if O(f(n) + g(n)), then the bigger asymptoptic growth determines big Oh

# R-3.15
# f(n) = O(g(n)) if and only if g(n) = BigOmega(f(n))
# f(n) <= cg(n) where c is a positive integer
# g(n) >= cf(n) where c is a positive integer
# Both are equal to each other

# R-3.16
# p(n) is a polynomial in n, then logp(n) is O(logn)
# Not completely sure how to interpret this ...
# Function p(n) is a polynomial in n, so p(n) = cn^d for some constant c and d?
# log(cn^d) = log(c) + log(n^d) = log(c) + dlog(n) which is O(logn)

# R-3.17
# (n+1)^5 = O(n^5)
# n^5 + 5n^4 + 10n^3 + 10n^2 + 5n + 1 = O(n^5)
# Since n^5 is the hightest degree and is equal to O(n^5), they are equal.

# R-3.18
# 2^(n+1) = O(2^n)
# 2^n + 2^1 = O(2^n)

# R-3.19
# Show that n is O(nlogn)
# n <= nlogn as n approaches infinity

# R-3.20
# Show that n^2 is Big Omega(nlogn)
# n^2 >= cnlogn for c > 0 as n appraches infinity

# R-3.21
# Show that nlogn is big Omega(n)
# nlogn >= cn for c > 0 as n appraches infinity

# R-3.22
# f(n) is O(f(n)) for when f(n) is greater than 1 and nondecreasing since
# f(n) <= c(f(n)) for c > 0

# R-3.23
"""
    def example1(S):
        n = len(S)
        total = 0
        for j in range(n):
            total += S[j]
        return total
"""
# Running Time:O(n) since the for loop is iterating over n elements in S

# R-3.24
"""
    def example2(S):
        n = len(S)
        total = 0
        for j in range(0, n, 2):
            total += S[j]
        return total
"""
# Running Time: O(n/2) = O(n) since the for loop is iterating over half of n elements in S

# R-3.25
"""
    def example3(S):
        n = len(S)
        total = 0
        for j in range(n):
            for x in range(1+j):
                total += S[k]
        return total
"""
# Running Time: O(n^2) since there are two for loops iterating over n elements in S

# R-3.27
"""
    def example5(A, B):
        n = len(A)
        count = 0
        for j in range(n):
            for x in range(1 + j):
                total += A[k]
            if B[i] == total:
                count += 1
        return count
"""
# Running Time: O(n) since there is one for loop iterating over n elements in A, comparisons are O(1) time

# R-3.28
# 1 second = 10^6 microseconds
# 1 minute = 60 seconds
# 1 hour = 60 minutes
# 1 day = 24 hours
# 1 month = 30 days
# 1 year = 12 months
# 1 century = 100 years
"""
    f(n) | 1 second | 1 hour | 1 month | 1 century
    -----|----------|--------|---------|----------
    logn | 2^(10^6) | 72^(10^8) | 5184^(10^9) | 62208^(10^11)
    n    | 10^6     | 36*10^8   | 2592*10^9   | 31104 * 10^11
    nlogn| 62746    | 2258856 * 10^2 | 162637632 * 10^3 | 1.9516516 * 10^14
    n^2  | 1000     | 36 * 10^5 | 2592 * 10^6 | 31104 * 10^8
    2^n  | ~20      | 72000  | 5184 * 10^3 | 62208 * 10^6
"""

# R-3.29
# Executes an O(logn) computation for each entry in n-element sequence
# Worst-case running time = O(nlogn)

# R-3.30
# Executes O(n) time calculation for each on logn random elements S
# Worst case running time = O(nlogn)

# R-3.31
# Executes O(n) time calculation for each even number in S
# Executes O(logn) time calculation for each odd number in S
# Worst case running time = O(n^2) if each number is even
# Best case running time = O(nlogn) if each number is odd

# R-3.32
# Given n element S
# Algorithm D calls Algorithm E on each element S[i]
# Algorithm E runs in O(i) time when called o element S[i]
# Worst case running time on Algorithm D = O(ni)
