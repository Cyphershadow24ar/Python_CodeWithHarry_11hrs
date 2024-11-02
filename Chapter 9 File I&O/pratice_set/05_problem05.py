#Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "bad", "Cool"]

with open("file.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("file.txt", "w") as f:
    f.write(content)