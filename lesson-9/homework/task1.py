class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = {}  
        self.members = {}

    def add_book(self, title, author):
        self.books[title] = Book(title, author)

    def add_member(self, name):
        self.members[name] = Member(name)

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book not found in the library.")
        if member_name not in self.members:
            print("Member not found. Please register first.")
            return
        member = self.members[member_name]
        book = self.books[book_title]
        member.borrow_book(book)
        print(f"{member_name} borrowed '{book_title}'.")

    def return_book(self, member_name, book_title):
        if member_name not in self.members or book_title not in self.books:
            print("Invalid return attempt.")
            return
        member = self.members[member_name]
        book = self.books[book_title]
        member.return_book(book)
        print(f"{member_name} returned '{book_title}'.")