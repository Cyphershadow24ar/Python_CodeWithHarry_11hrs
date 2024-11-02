class Employee:
    language = "py" # This is a class attributes.
    salary = 150000

    def getinfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

Aniket = Employee()
#Aniket.language = "JS"    # This is an object / instance attribute
# print(Aniket.language, Aniket.salary)

Aniket.greet()
Aniket.getinfo() #method 1
#Employee.getinfo(Aniket) #method 2

 

