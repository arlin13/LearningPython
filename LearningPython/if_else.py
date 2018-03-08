"""
Trusty and falsy values
Int
    0 = false
    > 0 or < 0 = true
String

    ==  checks equality
    is  checks if two variables are pointing to the same object in memory !!!

"""

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

# Multiple if conditions
if 13 > 8 and number_of_automation_test_by_me:
    print("Both are true")
if 13 > 8 or number_of_automation_test_by_me:
    print("Only one is true")
if 8 < 13 < 21 and True is 1 and False is 0:
    print("All statements are true")

# Ternary if statements
print("13 is greater than 8" if 13 > 8 else "13 is smaller than 8")
print("8 is greater than 13" if 8 > 13 else "8 is smaller than 13")
# How it works: X if condition is true, else Y
