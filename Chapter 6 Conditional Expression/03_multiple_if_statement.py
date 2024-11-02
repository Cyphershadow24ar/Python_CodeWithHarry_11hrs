a =int(input("Enter you age: "))

#if statement no.: 1 This statement or condition is gonna work on itself or we can it's independent.
if(a%2==0):
    print("A is even.")

else:
    print("A is odd.")

#End of IF statement NO. 1.

#if statement no.: 2 This statement is also independent of statement 1.
if(a>=18):
    print("Your are above the age of consent.")
    print("Good for you.")

elif(a<0):
    print("You are entering an invalid negative age.")

else:
    print("You are below the age of consent.")  

#end of IF statemnt no. 2.

print("\nEnd of program.")

#TODO: ELSE & ELIF cannot be used alone it can only be used with if BUT IF can be used alone.