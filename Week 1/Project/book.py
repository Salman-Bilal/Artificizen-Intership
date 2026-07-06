
class Book:
    def __init__(self, title: str, author: str, isbn: str, copies_available: int):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies_available = copies_available

    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def __str__(self) -> str:
        return f" '{self.title}' by {self.author} [ISBN: {self.isbn}] (Copies: {self.copies_available})"