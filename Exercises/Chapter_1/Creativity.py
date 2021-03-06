from random import randrange, choice, randint
import math

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

data = []
for i in range(0,11):
    data.append(i)
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

# C-1.23

def do_not_out_bound(data, i):
    try:
        print(data[i])
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")

bounded=[1,2,3]
# do_not_out_bound(bounded,3) # Don't try buffer overflow attacks in Python!

# C-1.24

def count_vowels(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

string = 'alphabet'
assert(count_vowels(string) == 3)

# C-1.25

def punc_out(string):
    punctuation = {',', '.', '!', '?'}
    unpunc = ''
    for i in string:
        if i not in punctuation:
            unpunc += i
    return unpunc

sentence = 'Hello, my name is Boop?'
assert(punc_out(sentence) == 'Hello my name is Boop')

# C-1.26

def formula(a, b, c):
    sum = lambda x,y: x + y
    subtr = lambda x,y: x - y
    mult = lambda x,y: x * y
    div = lambda x,y: x / y
    arithmetic = {sum, subtr, mult, div}

    for i in arithmetic:
        if i(a,b) == c or i(b,c) == a:
            return True
    return False

a = {3, 9, 2, 10}
b = {6, 6, 4, 2}
c = {9, 3, 8, 5}

assert(formula(a[i], b[i], c[i]) == True for i in range(0, 4))
assert(formula(c[i], b[i], a[i]) == True for i in range(0, 4))

d = 3
e = 5
f = 4

assert(formula(d,e,f) == False)

# C-1.27

def factors(n):
    k = 1
    pair = []
    while k * k < n:
        if n % k == 0:
            yield k
            pair = [k] + pair
        k += 1
    if k * k == n:
        yield k
    for i in pair:
        yield n // i

# C-1.28

def norm(v, p = 2):
    sum = 0
    for i in v:
        sum += pow(i, p)
    return math.sqrt(sum)

assert(norm([3,4]) == 5)
