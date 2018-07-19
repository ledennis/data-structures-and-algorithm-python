class User:
    def __init__(self, name):
        self._name = name
        self._library = Library()

    def read_book(self, book):
        if self._library.has_book(book):
            print(self._name + ' is reading ' + book.get_title() + '.')
        else:
            print(self._name + ' does not have ' + book.get_title() + '.')

    def get_library(self):
        return self._library

    def view_library(self):
        print(self._library.get_library())


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_information(self):
        return 'Title: ' + self.get_title() + ' , Author: ' + self.get_author()

class Library:
    def __init__(self):
        self._library = []

    def add_book(self, Book):
        self._library.append(Book)

    def has_book(self, Book):
        if Book in self._library:
            return True
        else:
            return False

    def get_book(self, Book):
        if self.has_book(Book):
            return Book
        else:
            print(Book._title + ' is not in your library.')

    def get_library(self):
        return self._library

class Store:
    def __init__(self, catalog=[]):
        self._catalog = catalog
        self._user_libraries = dict()

    def add_user(self, user):
        if user not in self._user_libraries:
            self._user_libraries[user] = Library()

    def add_books_catalog(self, books):
        for book in books:
            self.add_book_catalog(book)

    def add_book_catalog(self, book):
        if book not in self._catalog:
            self._catalog.append(book)
        else:
            raise AttributeError(book.get_information() + ' is already in the catalog.')

    def show_catalog(self, user):
        owned_books = self._user_libraries[user].get_library()
        for book in self._catalog:
            if book not in owned_books:
                print(book.get_information())

    def purchase_book(self, user, book):
        if book not in self._user_libraries[user].get_library():
            self._user_libraries[user].add_book(book)
            user.get_library().add_book(book)
        else:
            raise AttributeError('Something went wrong.')

if __name__ == '__main__':
    abigail = User('Abigail')
    jose = User('Jose')
    book_store = Store()
    book_one = Book('Flying Boops', 'Donovan Jackson')
    book_two = Book('Running Boops', 'Charlie Johnson')
    book_three = Book('Swimming Boops', 'Michaes Jackson')
    book_store.add_books_catalog([book_one, book_two, book_three])
    book_store.add_user(abigail)
    book_store.add_user(jose)
    book_store.show_catalog(abigail)
    book_store.purchase_book(abigail, book_one)
    book_store.purchase_book(jose, book_two)
    abigail.read_book(book_one)
    jose.read_book(book_two)
