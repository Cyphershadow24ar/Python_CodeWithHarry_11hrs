#Write a program to find the greatest of four numbers entered by the user.

a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
d=int(input("Enter number 4: "))

if(a>b and a>c and a>d):
    print("No. 1 is greatest",a)

elif(b>c and b>a and b>d):
    print("No.2 is greatest.",c)

elif(c>a and c>b and c>d):
    print("No.3 is greatest.",c)

# elif(d>a and d>b and d>c):
#     print("No.4 is the greatest.",d)

else:
    print("No.4 is the greatest.", d)