
import json
import os

def find_db():
    if not os.path.exists("students.json"):
        with open("students.json", "w") as file:
            json.dump([], file, indent=4)

def load_data():
    find_db()
    with open("students.json", "r") as file:
        return json.load(file)

def add_data(students):
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def register_student():
    students = load_data()
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == student_id:
            print("Error: Student ID already exists!")
            return

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    contact = input("Enter Contact Number: ")

    new_student = {
        "student_id": student_id,
        "student_name": name,
        "department": department,
        "contact": contact
    }

    students.append(new_student)
    add_data(students)
    print("Student registered successfully!")