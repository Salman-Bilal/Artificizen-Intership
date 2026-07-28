# member.py

class Member:
    def __init__(self, name: str, member_id: str, borrowed_books: list[str] = None):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books is not None else []

    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def __str__(self) -> str:
        return f" Member: {self.name} [ID: {self.member_id}] | Active Loans: {len(self.borrowed_books)}"