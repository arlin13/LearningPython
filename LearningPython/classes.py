"""
CLASSES
    # pass      # keyword, means 'do nothing'
    # self      # using self is the way we refer to our class from our class
    # __init__  # initialization, is the constructor of the class
    # __str___  # going to be called every time we print an instance of our class
"""

students_list = []


class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        students_list.append(self)

    def __str__(self):
        return "Student " + self.get_name_capitalize() + " " + self.get_last_name_capitalize()

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_last_name_capitalize(self):
        return self.last_name.capitalize()

    def get_school_name(self):
        return self.school_name


student = Student("arlin", "grijalba")
print(student)
# print(student.school_name)

print(Student.school_name)


# print(students_list)

# prints the memory space of that instance
# student1 = Student()
# student2 = Student()
# student3 = Student()
#
# print(student1)
# print(student2)
# print(student3)


# def add_student(self, name):
#     new_student = {"name": name}
#     students_list.append(new_student)
