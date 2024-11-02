#Write a python function to print multiplication table of a given number.

def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")

multiply(5)