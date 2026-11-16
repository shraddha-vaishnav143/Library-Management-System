import json
import os

def find_db():
    if not os.path.exists("issued_books.json"):
        with open("issued_books.json", "w") as file:
            json.dump([], file, indent=4)

def load_data():
    find_db()
    with open("issued_books.json", "r") as file:
        return json.load(file)

def add_data(issued_books):
    with open("issued_books.json", "w") as file:
        json.dump(issued_books, file, indent=4)


def issue_book():
    if not os.path.exists("books.json") or not os.path.exists("students.json"):
        print("Error: Please add books and register students first!")
        return

    with open("books.json", "r") as file:
        books = json.load(file)
    with open("students.json", "r") as file:
        students = json.load(file)

    issued_books = load_data()

    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")
    issue_date = input("Enter Issue Date (DD-MM-YYYY): ")

    student_found = False
    for student in students:
        if student["student_id"] == student_id:
            student_found = True
            break

    if not student_found:
        print("Student not found!")
        return

    for book in books:
        if book["book_id"] == book_id:
            if book["available_copies"] > 0:
                book["available_copies"] = book["available_copies"] - 1

                new_record = {
                    "student_id": student_id,
                    "book_id": book_id,
                    "issue_date": issue_date
                }
                issued_books.append(new_record)

                with open("books.json", "w") as file:
                    json.dump(books, file, indent=4)
                add_data(issued_books)

                print("Book issued successfully!")
                return
            else:
                print("Error: No copies available!")
                return

    print("Book not found!")


def return_book():
    if not os.path.exists("books.json"):
        print("No books found in library.")
        return

    with open("books.json", "r") as file:
        books = json.load(file)

    issued_books = load_data()

    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")

    for record in issued_books:
        if record["student_id"] == student_id and record["book_id"] == book_id:
            issued_books.remove(record)

            for book in books:
                if book["book_id"] == book_id:
                    book["available_copies"] = book["available_copies"] + 1
                    break

            with open("books.json", "w") as file:
                json.dump(books, file, indent=4)
            add_data(issued_books)

            print("Book returned successfully!")
            return

    print("Error: Issue record not found!")


def display_issued_books():
    issued_books = load_data()
    if not issued_books:
        print("No books issued yet.")
        return

    for record in issued_books:
        print("\n--------------------------")
        print("Student ID:", record["student_id"])
        print("Book ID:", record["book_id"])
        print("Issue Date:", record["issue_date"])