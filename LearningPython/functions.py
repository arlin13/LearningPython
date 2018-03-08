"""
FUNCTIONS
"""

print("I'm being printed by a function!")


# def imprimir(text):
#     print(text)


# def imprimir(text):
#     for t in text:
#         print(t)


# imprimir("I'm being printed by a custom function")


# Returning a value
print()
students = []


def print_students_total():
    print(f"Total of students: {len(students)}")


def print_students_list():
    print("List of students:")
    for student in students:
        id_to_print = "X" if student["student_id"] == 0 else student["student_id"]
        print(f"{id_to_print}: {student['name']}")


# optional parameter
def add_student(name, student_id=0):
    student = {"name": name, "student_id": student_id}
    students.append(student)
    print("New student added")
    print_students_total()
    print_students_list()
    print()


add_student('Arlin', 21)
add_student('Aidee', 29)
add_student('Arturo')
add_student('Anneth')
add_student('Alfredo', 16)
# also works as
add_student(name="Oliver")
add_student(name="Matthew", student_id=16)
add_student(student_id=14, name="Caleb")

print()
print("Arlin", 13, "Grijalba", True, None, 21)
# imprimir("Arlin", 13, "Grijalba")
