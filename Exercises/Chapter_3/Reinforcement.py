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
# Running Time:O(S) since the for loop is iterating over S elements

# R-3.23
"""
    def example2(S):
        n = len(S)
        total = 0
        for j in range(0, n, 2):
            total += S[j]
        return total
"""
# Running Time: O(S/2) = O(S) since the for loop is iterating over half of S elements
