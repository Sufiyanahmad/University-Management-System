import csv
import os

STUDENT_FILE = 'students.csv'
FACULTY_FILE = 'faculty.csv'

def init_files():
    for file, headers in [(STUDENT_FILE, ['ID', 'Name', 'Department', 'Year']),
                          (FACULTY_FILE, ['ID', 'Name', 'Department', 'Subject'])]:
        if not os.path.exists(file):
            with open(file, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)

def add_student():
    print("\n--- Add Student ---")
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    year = input("Enter Year: ")

    with open(STUDENT_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([sid, name, dept, year])
    print("✅ Student added successfully!\n")

def add_faculty():
    print("\n--- Add Faculty ---")
    fid = input("Enter Faculty ID: ")
    name = input("Enter Faculty Name: ")
    dept = input("Enter Department: ")
    subject = input("Enter Subject: ")

    with open(FACULTY_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([fid, name, dept, subject])
    print("✅ Faculty added successfully!\n")

def view_records(file, record_type):
    print(f"\n--- All {record_type} Records ---")
    try:
        with open(file, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("⚠️ No records found.")
    print()

def search_record(file, record_type):
    print(f"\n--- Search {record_type} ---")
    search_id = input(f"Enter {record_type} ID: ")
    found = False
    with open(file, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] == search_id:
                print(" | ".join(row))
                found = True
                break
    if not found:
        print("❌ Record not found.\n")

def delete_record(file, record_type):
    print(f"\n--- Delete {record_type} Record ---")
    delete_id = input(f"Enter {record_type} ID to delete: ")
    rows = []
    deleted = False

    with open(file, mode='r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and row[0] != delete_id:
                rows.append(row)
            else:
                deleted = True

    with open(file, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    if deleted:
        print("✅ Record deleted successfully.\n")
    else:
        print("❌ Record not found.\n")

def menu():
    init_files()
    while True:
        print("====== University Management System ======")
        print("1. Add Student")
        print("2. Add Faculty")
        print("3. View Students")
        print("4. View Faculty")
        print("5. Search Student by ID")
        print("6. Search Faculty by ID")
        print("7. Delete Student")
        print("8. Delete Faculty")
        print("9. Exit")
        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_faculty()
        elif choice == '3':
            view_records(STUDENT_FILE, "Student")
        elif choice == '4':
            view_records(FACULTY_FILE, "Faculty")
        elif choice == '5':
            search_record(STUDENT_FILE, "Student")
        elif choice == '6':
            search_record(FACULTY_FILE, "Faculty")
        elif choice == '7':
            delete_record(STUDENT_FILE, "Student")
        elif choice == '8':
            delete_record(FACULTY_FILE, "Faculty")
        elif choice == '9':
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

if __name__ == '__main__':
    menu()
