#Write a program which finds out whether a given name is 
#present in a list or not.

list =["harry", 'aniket', "raj", "ram", "don"]

name = input("Enter the name: ")

if(name in list ):
    print("The name is present in the list.")
else:
    print("The name is not present in the list.")