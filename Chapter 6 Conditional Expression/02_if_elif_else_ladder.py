#TODO: if elif else ladder

a =int(input("Enter you age: "))

if(a>=18):
    print("Your are above the age of consent.")
    print("Good for you.")

elif(a<0):
    print("You are entering an invalid negative age.")

elif(a==0):
    print("Yoou are entering 0 which is not a valid age.")

else:
    print("You are below the age of consent.")  

print("\nEnd of program.")

