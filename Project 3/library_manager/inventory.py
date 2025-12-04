import json
import logging
from pathlib import Path
from library_manager.book import Book


class LibraryInventory:
    def __init__(self, filename="catalog.json"):
        self.filename = filename
        self.books = self.load_data()

    # --------------------------------------------------------
    # Load book records from JSON (Task 3 + Task 5)
    # --------------------------------------------------------
    def load_data(self):
        try:
            path = Path(self.filename)

            # File not found → create empty list
            if not path.exists():
                logging.error("Catalog file not found. Creating a new one.")
                return []

            # Read JSON
            with open(self.filename, "r") as f:
                data = json.load(f)

            # Convert dict → Book objects
            return [Book(**book_dict) for book_dict in data]

        except json.JSONDecodeError:
            logging.error("Catalog file is corrupted. Resetting file.")
            return []

        except Exception as e:
            logging.error(f"Unexpected error during file read: {e}")
            return []

    # --------------------------------------------------------
    # Save data to JSON (Task 3 + Task 5)
    # --------------------------------------------------------
    def save_data(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([book.to_dict() for book in self.books], f, indent=4)

        except Exception as e:
            logging.error(f"Error writing to file: {e}")

    # --------------------------------------------------------
    # Add a new book
    # --------------------------------------------------------
    def add_book(self, book: Book):
        self.books.append(book)
        logging.info(f"Book added: {book.title}")
        self.save_data()

    # --------------------------------------------------------
    # Search book by title
    # --------------------------------------------------------
    def search_by_title(self, title):
        results = [book for book in self.books if title.lower() in book.title.lower()]
        logging.info(f"Search by title: {title} - {len(results)} result(s)")
        return results

    # --------------------------------------------------------
    # Search book by ISBN
    # --------------------------------------------------------
    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                logging.info(f"Search by ISBN: {isbn} - Book found")
                return book
        logging.warning(f"Search by ISBN: {isbn} - No book found")
        return None

    # --------------------------------------------------------
    # Issue a book (mark as issued)
    # --------------------------------------------------------
    def issue_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and book.is_available():
            book.issue()
            logging.info(f"Book issued: {isbn}")
            self.save_data()
            return True

        logging.warning(f"Failed to issue book: {isbn}")
        return False

    # --------------------------------------------------------
    # Return a book (mark as available)
    # --------------------------------------------------------
    def return_book(self, isbn):
        book = self.search_by_isbn(isbn)
        if book and not book.is_available():
            book.return_book()
            logging.info(f"Book returned: {isbn}")
            self.save_data()
            return True

        logging.warning(f"Failed to return book: {isbn}")
        return False

    # --------------------------------------------------------
    # Display all books
    # --------------------------------------------------------
    def display_all(self):
        return self.books

    # --------------------------------------------------------
    # Remove a book by ISBN
    # --------------------------------------------------------
    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                logging.info(f"Book removed: {isbn}")
                self.save_data()
                return True

        logging.warning(f"Tried removing non-existent book: {isbn}")
        return False
