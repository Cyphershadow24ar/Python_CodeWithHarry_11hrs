#A file contains a word “Donkey” multiple times. 
# You need to write a program which replace this word with ##### by updating the same file.

word = "Donkey"

with open("file.txt", "r") as f:
    content = f.read()

contentNew = content.replace("Donkey", "######")

with open("file.txt", "w") as f:
    f.write(contentNew)