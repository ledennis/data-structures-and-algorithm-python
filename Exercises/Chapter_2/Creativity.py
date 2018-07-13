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
