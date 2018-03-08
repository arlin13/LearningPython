"""
DICTIONARIES
Very easy to convert to JSON. They actually look like JSON
"""

print()
print("---- DICTIONARY ----")
me = {
    "Name": "Arlin",
    "DoB": "1991/08/21",
    "FavoriteColor": "Green",
    "FavoriteFood": "Tacos"
}
jr = {
    "Name": "Cesar",
    "DoB": "1985/09/23",
    "FavoriteColor": "Blue",
    "FavoriteFood": "Sea food"
}

print(me)
print(jr)

print()
print("Grouping dicitionaries together? Create a list of dicitionaries!")
cardona_people = [me, jr]
for person in cardona_people:
    print(f"{person['Name']} likes {person['FavoriteColor']} color and {person['FavoriteFood']}")

print()
print(f"First dictionary keys: {me.keys()}")
print(f"First dictionary values: {me.values()}")
