"""
LISTS
"""

students_names = []
students_names = ["Arlin", "Dan", "Chris"]

print(" ----- ACCESSING LIST ITEMS -----")
print("Printing first name with '[0]': {0}".format(students_names[0]))
print("Printing first name with '[-3]': {0}".format(students_names[-3]))
print("Printing second name with '[1]': {0}".format(students_names[1]))
print("Printing second name with '[-2]': {0}".format(students_names[-2]))
print(f"Printing third name with '[2]': {students_names[2]}")
print(f"Printing third name with '[-1]': {students_names[-1]}")

print()
print(" ----- REPLACING A LIST ITEM (VALUE) -----")
students_names[2] = "Jose"
print(f"Printing third and new name: {students_names[2]}")

print()
print(" ----- LENGTH OF LIST -----")
print(f"Length of list is {len(students_names)} : {students_names}")

print()
print(" ----- ADDING ITEMS TO LIST -----")
print("Adding Pamela to the list of students")
students_names.append("Pamela")
print(f"Students names array: {students_names}")
print(f"Printing last list item with '[-1]': {students_names[-1]}")

print()
print(" ----- CHECK IF ELEMENT EXISTS IN LIST -----")
if "Arlin" in students_names:
    print(f"Arlin is in the list: {students_names}")
else:
    print(f"Arlin is not in the list: {students_names}")
print()
if "Olga" in students_names:
    print(f"Olga is in the list: {students_names}")
else:
    print(f"Olga is not in the list: {students_names}")

print()
print(" ----- LENGTH OF LIST -----")
print(f"Length of list is {len(students_names)} : {students_names}")

print()
print(" ----- DELETING AN ITEMS FROM LIST -----")
print("Deleting Dan from list")
del students_names[1]
print(f"List: {students_names}")

print()
print(" ----- LIST SLICING -----")  # Select range of elements from list; Doesn't modify the list
print(f"Everyone except first person: {students_names[1:]}")
print(f"Everyone except last person: {students_names[:-1]}")
print(f"Everyone except first and last person: {students_names[1:-1]}")
students_names.append("Raul")
students_names.append("Ana")
students_names.append("Veronica")
print(f"Adding Raul, Ana and Veronica to the list: {students_names}")
print(f"Everyone except first person: {students_names[1:]}")
print(f"Everyone except last person: {students_names[:-1]}")
print(f"Everyone except first and last person: {students_names[1:-1]}")

