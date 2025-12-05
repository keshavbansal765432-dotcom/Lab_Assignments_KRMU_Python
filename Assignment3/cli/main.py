# cli/main.py

import logging
from pathlib import Path

from Library_manager import Book, LibraryInventory

# configure logging once for the whole app
LOG_FILE = Path("library.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("cli")


from pathlib import Path

from Library_manager import Book, LibraryInventory


def get_inventory() -> LibraryInventory:
    """Create a LibraryInventory that uses books.json in the project root."""
    storage_path = Path("books.json")
    return LibraryInventory(storage_path)

def prompt_int(message: str, min_value: int, max_value: int) -> int:
    while True:
        try:
            value = int(input(message))
            if value < min_value or value > max_value:
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu() -> None:
    print("\n=== Library Inventory Manager ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Books")
    print("6. Exit")


def main() -> None:
    inventory = get_inventory()

    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_book_flow(inventory)
        elif choice == "2":
            issue_book_flow(inventory)
        elif choice == "3":
            return_book_flow(inventory)
        elif choice == "4":
            view_all_flow(inventory)
        elif choice == "5":
            search_flow(inventory)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# ---- menu option functions (will fill now) ----

def add_book_flow(inventory: LibraryInventory) -> None:
    print("\n--- Add New Book ---")
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    isbn = input("ISBN: ").strip()

    if not title or not author or not isbn:
        print("All fields are required.")
        return

    book = Book(title=title, author=author, isbn=isbn)
    inventory.add_book(book)
    print("Book added successfully.")


def issue_book_flow(inventory: LibraryInventory) -> None:
    print("\n--- Issue Book ---")
    isbn = input("Enter ISBN to issue: ").strip()
    book = inventory.search_by_isbn(isbn)
    if book is None:
        print("Book not found.")
        return
    if book.issue():
        inventory.save_to_file()
        print("Book issued.")
    else:
        print("Book is already issued.")


def return_book_flow(inventory: LibraryInventory) -> None:
    print("\n--- Return Book ---")
    isbn = input("Enter ISBN to return: ").strip()
    book = inventory.search_by_isbn(isbn)
    if book is None:
        print("Book not found.")
        return
    if book.return_book():
        inventory.save_to_file()
        print("Book returned.")
    else:
        print("Book was not issued.")


def view_all_flow(inventory: LibraryInventory) -> None:
    print("\n--- All Books ---")
    books = inventory.display_all()
    if not books:
        print("No books in inventory.")
        return
    for b in books:
        print(b)


def search_flow(inventory: LibraryInventory) -> None:
    print("\n--- Search Books ---")
    print("1. Search by title")
    print("2. Search by ISBN")
    option = input("Choose option (1-2): ").strip()

    if option == "1":
        text = input("Enter title keyword: ").strip()
        results = inventory.search_by_title(text)
        if not results:
            print("No matching books found.")
        else:
            for b in results:
                print(b)
    elif option == "2":
        isbn = input("Enter ISBN: ").strip()
        book = inventory.search_by_isbn(isbn)
        if book is None:
            print("Book not found.")
        else:
            print(book)
    else:
        print("Invalid option.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.error("Unexpected error in CLI: %s", e)
        print("An unexpected error occurred. Please check library.log for details.")
