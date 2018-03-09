"""
YIELD
Used to pass/return (yield) value to caller function with every iteration
"""


def read_file():
    try:
        file = open("yield.txt", "r")
        # for line in file.readlines():
        # for line in read_line(file):
        for line in read_proper_nouns_line(file):
            print(line)
        file.close()
    except Exception as error:
        print(f"Could not read file: {error}")


# returns every line of file
def read_line(file):
    for line in file:
        yield line

# returns only first line: 'hola'
# def read_line(file):
#     for line in file:
#         return line


# own yield, only proper nouns
def read_proper_nouns_line(file):
    for line in file:
        if line[0].istitle():
            yield line


read_file()
