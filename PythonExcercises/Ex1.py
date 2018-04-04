"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

import datetime

now = datetime.datetime.now()
currentYear = now.year

name = input('Write your name: ')
age = input('Write your age: ')

yearsToTurn100 = 100 - int(age)

print(f'You will be 100 years old in year {currentYear+yearsToTurn100}')

