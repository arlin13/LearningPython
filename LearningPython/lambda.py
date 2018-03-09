"""
LAMBDA expression
Anonymous functions without a name or the 'def' keyword.
They return a value and can take arguments
"""


# functions that receives a number and returns the double
def double_of(number):
    return number * 2


print(f"Double of 13 is {double_of(13)}")
print(f"Double of 2 is {double_of(2)}")
print(f"Double of 5 is {double_of(5)}")


# lambda function that returns double of a number
double = lambda x: x * 2


print()
print(f"Double of 13 is {double(13)}")
