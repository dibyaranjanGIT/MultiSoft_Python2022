# create a MultiSoft Library
# Create a four methods inside this MS library
# display the books
# lend the book
# add book
# return book

## Constructor = ListOfbooks, library name

## create a dictionary to have the lenders name and book name

## Run a loop to ask the user to display the books, lend the book, add book and return book



# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library:
    def __init__(self, booklist, name):
        self.booksList = booklist
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        pass

    def lendBook(self, user, book):
        pass

    def addBook(self, book):
        pass

    def returnBook(self, book):
        pass

