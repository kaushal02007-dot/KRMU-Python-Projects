# Library Inventory Manager

**Submitted by:** Kaushal 

**Roll Number:** 2501730085

**Course:** Programming for Problem Solving using Python 

**Assignment Title:** Object-Oriented Design and Robust Programming in a Library Management System

**Submission Date:** 4 Dec, 2025


## Overview
A simple command-line Python application to manage a library's book inventory.  
It allows library staff to add books, issue and return them, search the catalog, and view all books.  
All data is stored persistently in a JSON file, and all actions are logged using Python's logging module.

---

## Features
- Add new books with title, author, and ISBN
- Issue books and mark them as issued
- Return books and mark them as available
- Search books by title keyword or ISBN
- View all books in the catalog
- Persistent storage using JSON (`catalog.json`)
- Logging of all operations and errors (`library.log`)
- Exception handling for invalid input and missing/corrupt files

---

## Folder Structure
library-inventory-manager/
│
├─ library_manager/
│ ├─ init.py
│ ├─ book.py
│ └─ inventory.py
│
├─ cli/
│ └─ main.py
├─ catalog.json
├─ library.log
├─ README.md
└─ requirements.txt

