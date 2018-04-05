"""
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""

user_input_numbers_list = input('Write numbers to add to your list. (Separated by comma): ')
user_input_lower_number = input('Write the lower number you want in your list:')
final_list = []

print(f'This is your list: {user_input_numbers_list}')
print(f'Numbers less than {user_input_lower_number}')


def numbers_less_than(all_numbers_list, lower_number):
    all_numbers_list = all_numbers_list.split(',')
    lower_number = int(lower_number)
    resulted_list = []

    for number in all_numbers_list:
        if int(number) <= lower_number:
            resulted_list.append(number)
    return resulted_list


final_list = numbers_less_than(user_input_numbers_list, user_input_lower_number)
print(f'Final list: {final_list}')
