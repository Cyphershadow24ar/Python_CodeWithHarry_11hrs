# write a program using functions to find greatest of three numbers.

#NOTE: METHOD 1 by ME
a =int (input("Enter the 1st Value: "))
b =int (input("Enter the 2nd Value: "))
c =int (input("Enter the 3rd Value: "))

def greatest(a,b,c):
    if(a>b and a>c):
        print(f"{a} is the greatest of all the three numbers.")
    elif(b>a and b>c):
        print(f"{b} is the greatest of all the three numbers.")
    elif(c>b and c>a):
        print(f"{c} is the greatest of all the three numbers.")
    else:
        print("Wrong data.")


greatest(a,b,c)


#NOTE: METHOD 2 by harry.
def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a = 1
b = 23
c = 3

print(greatest(a, b, c))