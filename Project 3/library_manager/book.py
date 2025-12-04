# Course            : Programming for Problem Solving using Python
# Assignment Title  : Object-Oriented Design and Robust Programming in a Library Management System
# Name              : Kaushal
# Roll no.          : 2501730085
# Section           : B
# School            : School of engineering technology(SOET)
# Submission date   : 4 Dec 2025

#_____________________________________________________________________________________________

class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status.lower()  

    def __str__(self):
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | Status: {self.status}"

    def to_dict(self):
        """Convert book object to dictionary for JSON storage."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

    def issue(self):
        """Mark the book as issued if available."""
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        """Mark the book as available if issued."""
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def is_available(self):
        """Check if the book is currently available."""
        return self.status == "available"