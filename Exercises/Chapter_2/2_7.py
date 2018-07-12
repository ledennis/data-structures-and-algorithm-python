# R-2.1
# 1. Fire Alarm
# 2. Pacemaker
# 3. Defibrillator

# R-2.2
# Whenever better hardware comes out, need to be able to port applications over with GUI updates to look fresh.
# If sofware is ran internationally, it must be flexible with different types of lawsselfself.

# R-2.3
# File tab of sublime. Methods are 'New Window', 'New File', 'Open ...', etc.

# R-2.4
class Flower:
    """ Flower class in R-2.4.

        name           name of Flower
        num_petals     number of petals
        price          price of Flower
    """

    def __init__(self, name, num_petals, price):
        """ Constructor for Flower. """
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def get_name(self):
        """ Return name of Flower. """
        return self._name

    def set_name(self, name):
        """ Set name of Flower. """
        self._name = name

    def get_num_petals(self):
        """ Return num_petals of Flower. """
        return self._num_petals

    def set_num_petals(self, num_petals):
        """ Set num_petals for Flower. """
        self._num_petals = num_petals

    def get_price(self):
        """ Return price of Flower. """
        return self._price

    def set_price(self, price):
        """ Set price for Flower. """
        self._price = price

# R-2.5
class CreditCard:
    """ A consumer credit card. pg 70. """

    def __init__(self, customer, bank, acnt, limit, balance = 0):
        """ Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer
        bank        the name of the bank
        acnt        the acount identifier
        limit       credit limit
        """

        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        # R-2.7
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_acnt(self):
        return self._acnt

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.
        """

        if isinstance(price, int) or isinstance(price, float):
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        else:
            raise ValueError('Can only charge with money.')

    def make_payment(self, amount):
        """ Process customer payment that reducces balance. """

        # R-2.6
        if (amount < 0):
            raise ValueError('Negative payment not allowed.')
        self._balance -= amount

# R-2.9
class Vector:
    """ Represent a vector in a multidimensional space. pg. 78 """

    def __init__(self, d):
        try:
            self._coords = [0] * len(d)
            for i in range(0, len(d)):
                self._coords[i] = d[i]
        except TypeError:
            try:
                self._coords = [0] * d
            except TypeError:
                raise TypeError('Wrong type')

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        """ Return sum of two vectors. """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    # R-2.9
    def __sub__(self, other):
        """ Return diff of two vectors. """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    # R-2.10
    def __neg__(self):
        """ Return inverse of vector. """
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result

    # R-2.12 && R-2.14
    def __mul__(self, other):
        """ Return mul of two vectors or mul each coord by num if num is int """
        if isinstance(other, int):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
        else:
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other[j]
            return result

    # R-2.13
    def __rmul__(self, other):
        """ Return mul of two vectors. """
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

# R-2.11
# Define __radd__ so that you can add a list to a vector with the list being on the left hand side.

# R-2.16
# max(0, (stop - start + step - 1) // step)
# First off, the zero is for if the start, stop, and step does not make sense, and returns a negative value.
# Second, the formula subtracts the start from stop, which is then equal to the length between the two.
# max(0, (length + step - 1) // step), where length = stop - start
# Third, since range is exclusive of the stop, step - 1 // step will remove the stop as an element.

# R-2.17
"""
    class Goat(object):
        instance variables:
            _tail
        methods:
            milk()
            jump()

    class Pig(object):
        instance variables:
            _nose
        methods:
            eat(food)
            wallow()

    class Horse(object):
        instance variables:
            _height
            _color
        methods:
            run()
            jump()

    class Equestrian(Horse):
        instance variables:
            _height     # inherited from Horse
            _color      # inherited from Horse
            _weight
        methods:
            run()       # inherited from Horse
            jump()      # inherited from Horse
            trot()
            is_trained()
"""

# R-2.18
# FibonaciProgression(2,2).print_progression(8)

# R-2.19
# Since 2^7 = 128, it will take 9 calls to get 2^63.

if __name__ == '__main__':
    # R-2.4
    redFlower = Flower('red', 12, 4)

    # Getters
    assert(redFlower.get_name() == 'red')
    assert(redFlower.get_num_petals() == 12)
    assert(redFlower.get_price() == 4)

    # Setters
    redFlower.set_name('blue')
    assert(redFlower.get_name() == 'blue')
    redFlower.set_num_petals(24)
    assert(redFlower.get_num_petals() == 24)
    redFlower.set_price(8)
    assert(redFlower.get_price() == 8)

    # R-2.5
    chase = CreditCard('Bob', 'Chase', '1234 5678 8765 4321', 4000)
    chase.charge(500.00)
    chase.charge(500)
    try:
        chase.charge('cookies')
        assert(False)
    except ValueError:
        assert(True)

    # R-2.6
    try:
        chase.make_payment(-789)
        assert(False)
    except ValueError:
        assert(True)

    # R-2.7
    wells = CreditCard('Kat', 'Fargo', '4312 1234 4312 1234', 5000, 10000)
    assert(wells.get_balance() == 10000)

    # R-2.8
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '1234 1234 1234 1234', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '1234 4567 1234 1234', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '1234 1234 7890 1234', 5000))

    for val in range(100, 116):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    assert(wallet[2].charge(3*116) == False)

    # R-2.9
    v = Vector(5)
    u = v - [1, 2, 3, 4, 5]
    w = Vector(5)
    w[0], w[1], w[2], w[3], w[4] = -1, -2, -3, -4, -5
    assert(u == w)

    # R-2.10
    y = Vector(5)
    y[0], y[1], y[2], y[3], y[4] = 1, 2, 3, 4, 5
    assert(-y == w)

    # R-2.12
    h = y * 2
    i = Vector(5)
    i[0], i[1], i[2], i[3], i[4] = 2, 4, 6, 8, 10
    assert(h == i)

    # R-2.13
    a = Vector(5)
    a[0], a[1], a[2], a[3], a[4] = -1, -4, -9, -16, -25
    b = [-1, -1, -1, -1, -1] * a
    assert(b == -a)

    # R-2.14
    z = y * w
    assert(z == a)

    # R-2.15
    m = Vector([4, 7 ,5])
    n = Vector(3)
    n[0], n[1], n[2] = 4, 7, 5
    assert(m == n)

    print(1 // 2)

    print(range(10,0, -2))
