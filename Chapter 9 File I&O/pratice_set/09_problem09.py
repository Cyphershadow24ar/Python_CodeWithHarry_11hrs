#Write a program to find out whether a file is 
# identical & matches the content of another file

with open("this.txt")as f: #example - file , this
    content1 =f.read()

with open("this_copy.txt")as f: #example - poem_P0 ,this_copy
    content2 =f.read()

if(content1 == content2):
    print("Print yes these files are identical.")

else:
    print("No this files are not identical.")