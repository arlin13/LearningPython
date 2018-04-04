"""
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
"""

number = int(input('Write a number: '))
# isEven = True if (int(number) % 2 == 0) else False

if number % 2 == 0:
    print(f'Number {number} is even')
else:
    print(f'Number {number} is odd')

