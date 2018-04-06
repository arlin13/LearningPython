"""
    Take two lists, say for example these two:
      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
      b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are common between the lists
    (without duplicates). Make sure your program works on two lists of different sizes.

    Extras:
    Randomly generate two lists to test this
    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

import random


def generate_random_list():
    length = random.randint(2, 15)
    random_list = []
    for i in range(1, length):
        random_list.append(random.randint(min_number, max_number))
    return random_list


min_number = input('Lower number (value): ')
max_number = input('Max number (value): ')

try:
    min_number = int(min_number)
    max_number = int(max_number)
except TypeError:
    print('Type valid numbers')

list1 = generate_random_list()
list2 = generate_random_list()

print(f'List 1: {list1}')
print(f'List 2: {list2}')

# Actually check common numbers
# TODO
print(f'Common numbers: {set(list1) & set(list2)}')

