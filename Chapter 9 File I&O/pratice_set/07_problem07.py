#Write a program to find out the 
#line number where python is present from ques 6.

with open("log.txt") as f:
    lines = f.readlines()  # Read all lines into a list

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes, Python is present. Line no: {lineno}")
        break
    lineno += 1
else:
    print("No, Python is not present.")
