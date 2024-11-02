#Create a class with a class attribute a; create an object 
# from it and set ‘a’ directly using ‘object.a = 0’. 
# Does this change the class attribute?


#NOTE: Answer -> NO the class attributes Does not changes.
class Demo:
    a=4

o = Demo()
print(o.a) #Prints the class attributes because instance attribute is not present.

o.a = 0 # Instance attribute is set
print(o.a) #Prints the instance attribute because instance attributes is not  present.

print(Demo.a) #prints the class attributes