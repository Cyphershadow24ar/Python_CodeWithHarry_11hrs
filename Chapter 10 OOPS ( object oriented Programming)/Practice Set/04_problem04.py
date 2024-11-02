#Add a static method in problem 2, 
# to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.n =float(n)

    def square(self):
        print(f"The Square is {self.n*self.n}.")

    def cube(self):
        print(f"The Cube is {self.n*self.n*self.n}")

    def Squareroot(self):
        print(f"The Square root is {self.n**1/2}")

    @staticmethod
    def greet():
        print("\n Thank you")

# a = Calculator(4) 
a = Calculator(input("Enter the Number: "))
a.square()
a.cube()
a.Squareroot()
a.greet()