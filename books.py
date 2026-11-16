
import json
import os


def find_db():
    if not os.path.exists("books.json"):
        with open("books.json", "w") as file:
            json.dump([], file, indent=4)


def load_data():
    find_db()
    with open("books.json", "r") as file:
        return json.load(file)


def add_data(books):
    with open("books.json", "w") as file:
        json.dump(books, file, indent=4)


def add_book():
    books = load_data()
    book_id = input("Enter Book ID: ")

    for book in books:
        if book["book_id"] == book_id:
            print("Error: Book ID already exists!")
            return

    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    category = input("Enter Category: ")
    copies = int(input("Enter Number of Copies: "))

    if copies <= 0:
        print("Number of copies must be greater than 0.")
        return

    new_book = {
        "book_id": book_id,
        "book_name": book_name,
        "author": author,
        "category": category,
        "available_copies": copies
    }

    books.append(new_book)
    add_data(books)
    print("Book added successfully!")


def display_books():
    books = load_data()
    if not books:
        print("No books available yet.")
        return

    for book in books:
        print("\n--------------------------")
        print("Book ID:", book["book_id"])
        print("Book Name:", book["book_name"])
        print("Author:", book["author"])
        print("Category:", book["category"])
        print("Available Copies:", book["available_copies"])


def search_book():
    books = load_data()
    query = input("Enter Book ID, Book Name, or Author Name to search: ").lower()
    found = False

    for book in books:
        if (query in book["book_id"].lower() or
                query in book["book_name"].lower() or
                query in book["author"].lower()):
            print("\n--- Book Found ---")
            print("Book ID:", book["book_id"])
            print("Book Name:", book["book_name"])
            print("Author:", book["author"])
            print("Category:", book["category"])
            print("Available Copies:", book["available_copies"])
            found = True

    if not found:
        print("Book not found!")


def delete_book():
    books = load_data()

    if os.path.exists("issued_books.json"):
        with open("issued_books.json", "r") as file:
            issued_books = json.load(file)
    else:
        issued_books = []

    book_id = input("Enter Book ID to delete: ")

    for record in issued_books:
        if record["book_id"] == book_id:
            print("Error: Cannot delete! This book is currently issued.")
            return

    for book in books:
        if book["book_id"] == book_id:
            books.remove(book)
            add_data(books)
            print("Book deleted successfully!")
            return

    print("Book ID not found!")