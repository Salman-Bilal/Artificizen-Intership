import json

from exception import BookNotFoundError, NoCopiesAvailableError, AlreadyBorrowedError, NotBorrowedError
from book import Book
from member import Member

class Library:
    def __init__(self, storage_file: str = "library_data.json"):
        self.storage_file = storage_file
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
        self.load_data()

    def load_data(self) -> None:
        try:
            with open(self.storage_file, "r", encoding="utf-8") as file:
                raw_data = json.load(file)
                for book_raw in raw_data.get("books", []):
                    b = Book.from_dict(book_raw)
                    self.books[b.isbn] = b
                for member_raw in raw_data.get("members", []):
                    m = Member.from_dict(member_raw)
                    self.members[m.member_id] = m
        except FileNotFoundError:
            self.books = {}
            self.members = {}

    def save_data(self) -> None:
        structured_data = {
            "books": [b.to_dict() for b in self.books.values()],
            "members": [m.to_dict() for m in self.members.values()]
        }
        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump(structured_data, file, indent=4)

    def add_book(self, title: str, author: str, isbn: str, copies: int) -> None:
        if isbn in self.books:
            self.books[isbn].copies_available += copies
        else:
            self.books[isbn] = Book(title, author, isbn, copies)
        self.save_data()
        print(f" Added copies successfully: {self.books[isbn]}")

    def add_member(self, name: str, member_id: str) -> None:
        if member_id in self.members:
            print("⚠️ Systems Alert: A member registry already claims this ID slot.")
            return
        self.members[member_id] = Member(name, member_id)
        self.save_data()
        print(f" Registered New Profile: {self.members[member_id]}")

    def search_book(self, query: str) -> list[Book]:
        return [
            book for book in self.books.values()
            if query.lower() in book.title.lower() 
            or query.lower() in book.author.lower() 
            or query == book.isbn
        ]

    def issue_book(self, member_id: str, isbn: str) -> None:
        if member_id not in self.members:
            print(" System Error: Member profile not registered.")
            return
        if isbn not in self.books:
            raise BookNotFoundError(isbn)
            
        member = self.members[member_id]
        book = self.books[isbn]

        if book.copies_available <= 0:
            raise NoCopiesAvailableError(book.title)
        if isbn in member.borrowed_books:
            raise AlreadyBorrowedError(member.name, book.title)

        book.copies_available -= 1
        member.borrowed_books.append(isbn)
        self.save_data()
        print(f" Loan Approved! '{book.title}' checked out to {member.name}.")

    def return_book(self, member_id: str, isbn: str) -> None:
        if member_id not in self.members:
            print(" System Error: Member profile not registered.")
            return
        if isbn not in self.books:
            raise BookNotFoundError(isbn)

        member = self.members[member_id]
        book = self.books[isbn]

        if isbn not in member.borrowed_books:
            raise NotBorrowedError(member.name, book.title)

        book.copies_available += 1
        member.borrowed_books.remove(isbn)
        self.save_data()
        print(f" Return Processed! '{book.title}' dropped back into system storage by {member.name}.")