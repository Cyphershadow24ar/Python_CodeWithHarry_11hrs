#write a program to read the text from a gievn file 'poems.txt 

f = open("poem_P01.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()
