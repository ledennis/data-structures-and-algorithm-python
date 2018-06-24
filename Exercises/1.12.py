from random import randrange, choice

# R-1.1

def is_multiple(n, m):
    return m % n == 0

assert(is_multiple(2, 4) == True)
assert(is_multiple(3, 4) == False)

# R-1.2

def is_even(k):
    while(k > 0):
        k -= 2
    return k == 0

assert(is_even(100) == True)
assert(is_even(101) == False)

# R-1.3

def minmax(data):
    min = max = data[0]
    for i in data:
        if (i > max):
            max = i
        if (i < min):
            min = i
    return (min, max)

data = [2,4,9,5,1,8]
assert(minmax(data) == (1, 9))

# R-1.4 && R-1.5

def sum_squares(k):
    return sum([i*i for i in range(1, k)])

assert(sum_squares(3) == 5)
assert(sum_squares(8) == 140)
assert(sum_squares(10) == 285)

# R-1.6 && R-1.7

def sum_squares_odd(k):
    return sum([i*i for i in range(1, k) if i % 2 != 0])

assert(sum_squares_odd(3) == 1)
assert(sum_squares_odd(8) == 84)
assert(sum_squares_odd(10) == 165)

# R-1.8
# j is abs(k) if string s has length n, and expression s[k] is used for index -n <= k < 0, s[j] where j >= 0.

# R-1.9
assert(range(50, 90, 10) == [50, 60, 70, 80])

# R-1.10
assert(range(8, -10, -2) == [8, 6, 4, 2, 0, -2, -4, -6, -8])

# R-1.11
assert([pow(2, i) for i in range(0, 9)] == [1, 2, 4, 8, 16, 32, 64, 128, 256])

# R-1.12
def range_choice(data):
    return data[randrange(0, len(data))]

data = []
for i in range(0,11):
    data.append(i)

assert(range_choice(data) in data)
