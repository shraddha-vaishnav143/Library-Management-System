
import books
import students
import transactions

def main():
    books.find_db()
    students.find_db()
    transactions.find_db()
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add New Book")
        print("2. Display All Books")
        print("3. Search for a Book")
        print("4. Register a Student")
        print("5. Issue a Book")
        print("6. Return a Book")
        print("7. Display Issued Books")
        print("8. Delete a Book")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            books.add_book()

        elif choice == "2":
            books.display_books()

        elif choice == "3":
            books.search_book()

        elif choice == "4":
            students.register_student()

        elif choice == "5":
            transactions.issue_book()

        elif choice == "6":
            transactions.return_book()

        elif choice == "7":
            transactions.display_issued_books()

        elif choice == "8":
            books.delete_book()

        elif choice == "9":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()