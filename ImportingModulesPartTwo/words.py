from urllib.request import urlopen

with urlopen("https://textfiles.com/100/gems.txt") as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

for word in story_words:
    print(word)


print('hi arlin')


# import urllib.request
# with urllib.request.urlopen('http://python.org/') as response:
#     html = response.read()
# print(html)
