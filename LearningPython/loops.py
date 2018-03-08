"""
LOOPS
Python has 2 types: For loop and while loops.
"""
print()
print("---- F_O_R ----")
print()
print()
# Print "The value of X is #". # should increment by 10, from 10 to 100
print("----- FOR (1 to 10) -----")
x = 10
for index in range(10):
    print(f"The value of x is {x}")
    x += 10

# What does range function do?
# It basically takes whatever number you passed it and kind of converts it to a list
# Above, it would be something like this: [0,1,2,3,4,5,6,7,8,9]
# Think of that number as the number of times you want to iterate / execute the for loop

range(5, 10)  # from 5 to 10: [5,6,7,8,9]
range(5, 10, 2)  # from 5 to 10 and in increments by 2 [5,7,9]

print()
print("----- FOR (with a list) -----")
fav_numbers = [6, 8, 9, 11, 13, 16, 21, 22, 23, 29, 91, 1965, 1967, 1991, 1992, 1996, 2001, 2002]
print(f"These are my favorite numbers: {fav_numbers}")
print("Printing all of them with for:")
for number in fav_numbers:
    print(f"{number}")

print()
print("----- BREAK AND CONTINUE -----")
print("Print all numbers:")
for number in fav_numbers:
    print(number)
print()
print("Print all numbers until 13 is found:")
for number in fav_numbers:
    print(number)
    if number == 13:
        break
print()
print("Print all numbers except those that are NOT pair:")
for number in fav_numbers:
    if number % 2 != 0:
        continue
    print(number)


print()
print()
print()
print("---- W_H_I_L_E ----")
print()
number_13_was_found = False
index = 0
while not number_13_was_found:
    if fav_numbers[index] == 13:
        print(f"Value 13 was found at position: {index}")
        number_13_was_found = True
    index += 1
