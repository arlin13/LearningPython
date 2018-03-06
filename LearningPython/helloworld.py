"""Learning python!"""

print("hello world")
print("Hello Arlin, welcome")


def add_numbers(a: int, b: int) -> int:
    return a + b


total = add_numbers(8, 13)
print(total)


#total2 = add_numbers(13, 'a')
#print(total2)


def print_hello_world() -> str:
    return "Hello World!"


print_hello_world()
