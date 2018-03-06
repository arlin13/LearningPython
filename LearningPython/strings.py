# strings

# CHECK WHY STRING UTILITY METHODS ARE NOT WORKING AS I EXPECTED

first_name = "Arlin"
last_name = "Grijalba"

print(first_name, last_name)

first_name_capitalized = first_name.capitalize()
print(first_name_capitalized)

first_name_letter_a_replaced = first_name.replace("a", "e")
print(first_name_letter_a_replaced)

if last_name.isalpha:
    print('Letters!')
else:
    print('Numbers!')

if not last_name.isalpha:
    print('Numbers!')
else:
    print('Letters!')

# STRING FORMAT (Supports padding, printing class attributes...)

first_name_text = "Hi, I'm {0}".format(first_name)  # prints Hi, I'm Arlin
print(first_name_text)

whole_name_text = "Hi, I'm {0} {1}".format(first_name, last_name)  # prints Hi, I'm Arlin Grijalba
print(whole_name_text)

my_last_name_3_times = "{0} {1} {2}".format(last_name, last_name, last_name)  # prints Grijalba Grijalba Grijalba
print(my_last_name_3_times)

# STRING INTERPOLATION (So cool!)
print(f"Hi {first_name}")
print(f"Hi {first_name} {last_name}")
