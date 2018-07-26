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
