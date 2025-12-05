# library_manager/inventory.py

import json
from pathlib import Path
from typing import List, Optional

from .book import Book


class LibraryInventory:
    def __init__(self, storage_path: Path):
        # storage_path is where books.json will be stored
        self.storage_path = storage_path
        self.books: List[Book] = []
        # when object is created, try to load existing data
        self.load_from_file()

    # ---------- core operations (Task 2) ----------

    def add_book(self, book: Book) -> None:
        """Add a new Book object to the inventory."""
        self.books.append(book)
        # also save to file so data is not lost
        self.save_to_file()

    def search_by_title(self, title: str) -> List[Book]:
        """Return all books whose title contains the search text (case-insensitive)."""
        title_lower = title.lower()
        return [b for b in self.books if title_lower in b.title.lower()]

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        """Return the book whose ISBN matches exactly, or None if not found."""
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self) -> List[Book]:
        """Return the full list of books."""
        return self.books

    # ---------- file persistence with JSON (Task 3) ----------

    def load_from_file(self) -> None:
        """Load book list from JSON file, handling missing/corrupted file."""
        try:
            if not self.storage_path.exists():
                # file not present => start with empty inventory
                self.books = []
                return

            with self.storage_path.open("r", encoding="utf-8") as f:
                data = json.load(f)

            # convert list of dicts to list of Book objects
            self.books = [Book.from_dict(item) for item in data]

        except json.JSONDecodeError:
            # file is corrupted or not valid JSON
            print("Warning: JSON file is corrupted. Starting with empty list.")
            self.books = []
        except Exception as e:
            # any other unexpected error
            print("Error while loading file:", e)
            self.books = []

    def save_to_file(self) -> None:
        """Save current book list into JSON file."""
        try:
            # convert each Book to a dict, then dump list to JSON
            data = [b.to_dict() for b in self.books]
            with self.storage_path.open("w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except Exception as e:
            print("Error while saving file:", e)
