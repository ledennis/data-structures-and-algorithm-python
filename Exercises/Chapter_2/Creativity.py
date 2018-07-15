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

if __name__ == '__main__':
    # C-2.26
    seq = [1,2,3,4,5]
    revIt = ReverseSequenceIterator(seq)

    for i in range(0, 5):
        assert(next(revIt) == seq[len(seq) - 1 - i])

    # C-2.27
    print(2 in Range(2000000))
    print(2000000 in Range(2000000))
