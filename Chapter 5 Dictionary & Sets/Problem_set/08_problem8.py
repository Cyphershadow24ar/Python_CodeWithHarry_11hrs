#If language of two friends are same; what will happen to the program in problem 6?
#TODO: ANSWER - no change will occur in this case. the values can be same .

#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names.
# Assume that the names are unique.

d = {}

name= input("Enter friends name: ")
lang= input("Enter language name: ")
d.update({name: lang})

name= input("Enter friends name: ")
lang= input("Enter language name: ")
d.update({name: lang})

name= input("Enter friends name: ")
lang= input("Enter language name: ")
d.update({name: lang})

name= input("Enter friends name: ")
lang= input("Enter language name: ")
d.update({name: lang})

print(d)