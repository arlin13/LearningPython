"""
EXCEPTIONS
"""

print("---- EXCEPTIONS ----")
me = {
    "Name": "Arlin",
    "DoB": "1991/08/21",
    "FavoriteColor": "Green",
    "FavoriteFood": "Tacos"
}

print()
print("When trying to do:")
print("     $ last_name = me['LastName']")
print("Console prints:")
print("     last_name = me['LastName']")
print("     KeyError: 'LastName'")
# last_name = me["LastName"]

print()
print("--- Preventing exceptions ---")
try:
    last_name = me["last_name"]
except KeyError:
    print("Error finding last_name!")
print("This code executes!")

print()
print("--- Preventing more than one type of exception ---")
try:
    DoB = me["DoB"]
    letter_plus_number = 13 + 'Arlin'
except KeyError:
    print("Error finding last_name!")
except TypeError:
    print("You can't add number and strings")


print()
print("--- Preventing general exception ---")
try:
    letter_plus_number = 13 + 'Arlin'
except Exception:
    print("You can't add number and strings")


print()
print("--- Printing actual error ---")
try:
    letter_plus_number = 13 + 'Arlin'
except TypeError as error:
    print(f"Error was: {error}")
