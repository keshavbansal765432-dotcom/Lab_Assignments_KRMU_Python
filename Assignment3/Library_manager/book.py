# library_manager/book.py

class Book:
    def __init__(self, title: str, author: str, isbn: str, status: str = "available"):
        # attributes
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status  # "available" or "issued"

    def __str__(self) -> str:
        # how the book will print as text
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {self.status}"

    def to_dict(self) -> dict:
        # convert object to a normal dict (for JSON)
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status,
        }

    @classmethod
    def from_dict(cls, data: dict):
        # create Book object back from a dict
        return cls(
            title=data.get("title", ""),
            author=data.get("author", ""),
            isbn=data.get("isbn", ""),
            status=data.get("status", "available"),
        )

    def issue(self) -> bool:
        # mark book as issued if it is available
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self) -> bool:
        # mark book as available if it was issued
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self) -> bool:
        # check if the book is free to issue
        return self.status == "available"
