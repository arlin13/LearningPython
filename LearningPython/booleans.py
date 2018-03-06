# Python booleans

python_course = True
java_course = False

print(python_course)

print()

# True is 1
print("Is this a python course?")
if python_course == 1:
    print(int(python_course))
else:
    if python_course == 0:
        # False is 0
        print(int(python_course))

print("Is this a python course?")
if python_course:
    print("Yes")
else:
    print("No")

print()

# False is 0
print("Is this a java course?")
if java_course == 1:
    print(int(java_course))
else:
    if java_course == 0:
        # False is 0
        print(int(java_course))

print("Is this a java course?")
if java_course:
    print("Yes")
else:
    print("No")

print()

# NONE value
number_of_automation_test_by_me = None
print(number_of_automation_test_by_me)
if number_of_automation_test_by_me:
    print("None value is falsy")


# Not If
if not number_of_automation_test_by_me:
    print("None value is falsy")
if number_of_automation_test_by_me is not None:
    print("None value is falsy")
