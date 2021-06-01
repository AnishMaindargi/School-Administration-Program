import csv

Student_fields = ['roll', 'name', 'age', 'email', 'phone']
Student_database = 'students.csv'


def display_menu():
    print("**************************************")
    print(" Welcome to Student Management System")
    print("**************************************")
    print("1. Add New Student")
    print("2. View Students Information")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


def add_student():
    print("**************************************")
    print("Add Student Information")
    print("**************************************")
    global Student_fields
    global Student_database

    student_data = []
    for field in Student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(Student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_students():
    global Student_fields
    global Student_database

    print("*** Student Records ***")

    with open(Student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in Student_fields:
            print(x, end='\t |')
        print("\n**************************************")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def search_student():
    global Student_fields
    global Student_database

    print("--- Search Student ---")
    roll = input("Enter roll no. to search: ")

    with open(Student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Age: ", row[2])
                    print("Email: ", row[3])
                    print("Phone: ", row[4])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any key to continue")


def update_student():
    global Student_fields
    global Student_database

    print("*** Update Student ***")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []

    with open(Student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in Student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1