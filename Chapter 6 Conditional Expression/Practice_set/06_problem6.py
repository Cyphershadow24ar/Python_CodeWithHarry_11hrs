#Write a program to calculate the grade of a student from his
# marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

# marks = int(input("Enter the marks scored by the student: "))

# if marks > 100 or marks < 0:
#     print("Invalid marks. Please enter a value between 0 and 100.")

# elif marks >= 90:
#     print("The Grade is Ex.")

# elif marks >= 80:
#     print("The Grade is A.")

# elif marks >= 70:
#     print("The Grade is B.")

# elif marks >= 60:
#     print("The Grade is C.")

# elif marks >= 50:
#     print("The Grade is D.")

# else:
#     print("The Grade is F.")

marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    grade = "Ex"
elif(marks<90 and marks>=80):
    grade = "A"
elif(marks<80 and marks>=70):
    grade = "B"
elif(marks<70 and marks>=60):
    grade = "C"
elif(marks<60 and marks>=50):
    grade = "D"
elif(marks<50):
    grade = "F"

print("Your grade is:", grade)