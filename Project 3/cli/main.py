import logging
from library_manager.book import Book
from library_manager.inventory import LibraryInventory

# ----------------------------
# Logging setup (only once)
# ----------------------------
logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------
# Menu display
# ----------------------------
def display_menu():
    print("\n=== Library Inventory Manager ===")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

# ----------------------------
# Add book UI
# ----------------------------
def add_book_ui(inventory):
    print("\n--- Add a New Book ---")
    title = input("Enter title: ").strip()
    author = input("Enter author: ").strip()
    isbn = input("Enter ISBN: ").strip()

    if not title or not author or not isbn:
        print("❌ All fields are required!")
        return

    new_book = Book(title, author, isbn)
    inventory.add_book(new_book)
    print("✔ Book added successfully.")
    logging.info(f"Book added: {title}")

# ----------------------------
# Issue book UI
# ----------------------------
def issue_book_ui(inventory):
    isbn = input("\nEnter ISBN to issue: ").strip()
    success = inventory.issue_book(isbn)
    if success:
        print("✔ Book issued successfully.")
    else:
        print("❌ Book not found or already issued.")

# ----------------------------
# Return book UI
# ----------------------------
def return_book_ui(inventory):
    isbn = input("\nEnter ISBN to return: ").strip()
    success = inventory.return_book(isbn)
    if success:
        print("✔ Book returned successfully.")
    else:
        print("❌ Book not found or not issued.")

# ----------------------------
# Search book UI
# ----------------------------
def search_book_ui(inventory):
    keyword = input("\nEnter title keyword to search: ").strip()
    results = inventory.search_by_title(keyword)

    if not results:
        print("❌ No books found.")
        return

    print("\n--- Search Results ---")
    for book in results:
        print(book)

# ----------------------------
# View all books UI
# ----------------------------
def view_all_ui(inventory):
    print("\n--- All Books in Catalog ---")
    all_books = inventory.display_all()

    if not all_books:
        print("No books in inventory.")
        return

    for book in all_books:
        print(book)

# ----------------------------
# Main function
# ----------------------------
def main():
    inventory = LibraryInventory()  # loads data automatically in __init__

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                add_book_ui(inventory)
            elif choice == "2":
                issue_book_ui(inventory)
            elif choice == "3":
                return_book_ui(inventory)
            elif choice == "4":
                view_all_ui(inventory)
            elif choice == "5":
                search_book_ui(inventory)
            elif choice == "6":
                print("Exiting program...")
                inventory.save_data()
                break
            else:
                print("❌ Invalid choice. Enter 1–6.")

        except Exception as e:
            logging.error(f"Error during operation: {e}")
            print("❌ An unexpected error occurred.")

        # Save after every operation
        inventory.save_data()

# ----------------------------
# Run the program
# ----------------------------
if __name__ == "__main__":
    main()


