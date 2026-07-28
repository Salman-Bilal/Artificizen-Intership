
class BookNotFoundError(Exception):
    def __init__(self, isbn: str):
        super().__init__(f" Search Failure: No book found matching ISBN '{isbn}'.")

class NoCopiesAvailableError(Exception):
    def __init__(self, title: str):
        super().__init__(f" Inventory Exhausted: '{title}' has zero copies available to rent.")

class AlreadyBorrowedError(Exception):
    def __init__(self, name: str, title: str):
        super().__init__(f" Policy Violation: {name} is already holding a copy of '{title}'.")

class NotBorrowedError(Exception):
    def __init__(self, name: str, title: str):
        super().__init__(f" Transaction Refused: {name} cannot return '{title}' as it isn't on their profile.")