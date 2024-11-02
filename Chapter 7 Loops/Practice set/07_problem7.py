# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n = int(input("Enter the value: "))

for i in range (1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1),  end="") # LOGIC : 2*I-1 is used for odd type printing only.
    print("")
