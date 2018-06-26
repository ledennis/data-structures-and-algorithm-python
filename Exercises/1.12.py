from random import randrange, choice, randint

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

# C-1.13

def reverse(data):
    for i in range(0, len(data)/2):
        data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]
    return data

def reverse_one_line(data):
    return [data[len(data) - 1 - i] for i in range(len(data)-1, -1, -1)]

# assert(list(reverse(data)) == list(reversed(data)))
# assert(reverse_one_line(data) == list(reversed(data)))

# C-1.14

def find_odd_products(data):
    odd_products = {}
    for i in data:
        for j in data:
            if i * j % 2 != 0:
                odd_products[i] = j
    return odd_products

odd_products = find_odd_products(data)

for key in odd_products:
    assert(key * odd_products[key] % 2 != 0)

# C-1.15

def distinct(data):
    for i in data:
        check = data
        check.remove(i)
        if i in check:
            return False
    return True

distinct_set = [1,2,3]
not_distinct_set = [1,1,2,2]

assert(distinct(distinct_set) == True)
assert(distinct(not_distinct_set) == False)

# C-1.16
# The parameter contains a list and the references are being updated.

# C-1.17
# No because this implementation does not update the refernces in the data iterable object or return one.

# C-1.18
list_plus_two = [i + (pow((i),2)) for i in range(0, 10)]
assert(list_plus_two == [0,2,6,12,20,30,42,56,72,90])

# C-1.19

alphabet = [chr(i) for i in range(97, 123)]
assert(alphabet == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

# C-1.20

def shuffle_randint(data):
    for i in range(0, len(data)/2):
        swap_one = randint(0, len(data)-1)
        swap_two = randint(0, len(data)-1)
        data[swap_one], data[swap_two] = data[swap_two], data[swap_one]

shuffle = [1,2,3,4,5,6,7,8,9,10]
shuffle_randint(shuffle)
assert(shuffle != [1,2,3,4,5,6,7,8,9,10])

# C-1.21

def reverse_input():
    inputs = []
    try:
        while(True):
            new_input = input('Type Somthing')
            inputs.append(new_input)
    except EOFError:
        print(i for i in inputs)

# C-1.22

def dot_products(a, b):
    if (len(a) == len(b)):
        c = [0]*len(a)  # Initialize with length a
        for i in range(0, len(a)):
            c[i] = a[i] * b[i]
        return c
    else:
        raise ValueError('Length of arrays must be equal.')

a = b = [1,2,3]
assert(dot_products(a, b) == [1,4,9])

# c = [1,2,3]
# d = [1,2]
# e = dot_products(c,d) # Raises ValueError exception.
