#Write a class “Calculator” capable of finding square,
#  cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n =float(n)

    def square(self):
        print(f"The Square is {self.n*self.n}.")

    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")

    def Squareroot(self):
        print(f"The Square root is {self.n**1/2}")

# a = Calculator(4) 
a = Calculator(input("Enter the Number: "))
a.square()
a.cube()
a.Squareroot()