"""
Students app
Ask the user if he wants to add students info
If he says yes, add student to a list and keep asking for new student info
If says no, print current student list
"""

students_list = []


def ask_if_add_new_student():
    answer = True
    while answer != 'Y' or answer != 'N':
        print("\nDo you want to add a new student?")
        answer = input("Write 'Y' for yes, and 'N' for No: ")
        if answer == 'Y' or answer == 'y':
            return True
        elif answer == 'N' or answer == 'n':
            return False
        else:
            print("Error: Invalid input\n")


def ask_student_info():
    name = input("Student name: ")
    last_name = input("Student last name: ")
    age = input("Student age: ")
    add_student(name, last_name, age)


def add_student(name, last_name, age):
    new_student = {"id": len(students_list)+1, "name": name, "last_name": last_name, "age": age}
    students_list.append(new_student)
    save_student_to_file(new_student)


def print_students_list():
    print("\nStudents list:")
    for student in students_list:
        print(f"ID: {student['id']}. Name: {student['name']} {student['last_name']}. Age: {student['age']}")


def save_student_to_file(student):
    try:
        file = open("students.txt", "a")  # 'a' appends to a file, 'w' writes/replace all the text of a file
        file.write(f"ID: {student['id']}. Name: {student['name']} {student['last_name']}. Age: {student['age']} \n")
        file.close()
    except Exception:
        print("Could not save file")

#
# def read_file():
#     try:
#         file = open("students.txt", "r")
#         for student in file.readlines():
#


print("Welcome to Students app in python!")

while ask_if_add_new_student():
    ask_student_info()
print_students_list()
print("bye")
