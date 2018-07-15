# C-2.24
"""
    class Customer(object):
        variables:
            Name
            Email Address
            BankAcc
            Library

        methods:
            readBook()
            viewStore()
            viewLibrary()

    class Library(object):
        variables:
            libraryList[]
        methods:
            addBook()
            removeBook()
            printLibrary()

    class Store(object):
        variables:
            catalog
        methods:
            addBook()
            removeBook()
            printCatalog(Library)
            buyBook(Library)

    class Book(object):
        variables:
            Title
            Author
            Illustrator
            Publisher
            ID
            Genre
            Content
        method:
            printContent()

    class SoldBook(Book):
        variables:
            PurchaseDate
        method:
            printPurchaseDate

"""
# C-2.25 Implemented in Reinforcemnet.py.
"""
    # R-2.12 && R-2.14
    def __mul__(self, other):
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
"""

# C-2.26
"""
class SequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1

    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        return self
"""

class ReverseSequenceIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(sequence)

    def __next__(self):
        self._k -= 1
        if self._k in range(0, len(self._seq)):
            return(self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        return self

# C-2.27
class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start

        self._length = max(0, (stop - start + step - 1) // step)

        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range.')

        return self._start + k * self._step

    def __contains__(self, k):
        return k < self._length

# C-2.28 && C-2.29 && C-2.30
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

    def _set_balance(self, amount):
        self._balance += amount

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

class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._monthly_charges = 0
        self._monthly_fee = 0

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        self._monthly_charges += 1

    def process_month(self):
        additions = 0
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1/12)
            additions *= monthly_factor
        if self._monthly_charges > 10:
            additions += self._monthly_charges - 10
        if self._monthly_fee > 0:
            additions += 25

        super()._set_balance(additions)
        self._monthly_charges = 0
        self.set_monthly_fee()

    def set_monthly_fee(self):
        self._monthly_fee = self._balance * .10

    def get_monthly_fee(self):
        return self._monthly_fee

    def make_payment(self, amount):
        super().make_payment(amout)
        self._monthly_fee -= amount


class Progression:
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

# C-2.31
class AbsDiffProgression(Progression):
    def __init__(self, first=2, second=200):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev, self._current = self._current, abs(self._prev - self._current)

# C-2.32
class SquareRootProgression(Progression):
    def __init__(self, first=65536):
        super().__init__(first)

    def _advance(self):
        self._current = pow(self._current, .5)


if __name__ == '__main__':
    # C-2.26
    # seq = [1,2,3,4,5]
    # revIt = ReverseSequenceIterator(seq)
    #
    # for i in range(0, 5):
    #     assert(next(revIt) == seq[len(seq) - 1 - i])

    # C-2.27
    a = 2 in Range(2000000)
    assert(a == True)
    b = 2000000 in Range(2000000)
    assert(b == False)

    pred = PredatoryCreditCard('Bob', 'Chase', '1234123412341234', 5000, .0825)
    for i in range(0,15):
        pred.charge(50)
    pred.process_month()
    pred.process_month()

    # C-2.31
    adp = AbsDiffProgression()
    seq = [2, 196, 194, 2, 192, 190, 2, 188, 186, 2]
    for i in range(len(seq)):
        assert(next(adp) == seq[i])

    # C-2.32
    sqrp = SquareRootProgression()
    seq = [65536, 256, 16, 4, 2]
    for i in range(len(seq)):
        assert(next(sqrp) == seq[i])
