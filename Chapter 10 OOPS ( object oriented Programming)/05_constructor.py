class Employee:
    language = "py" # This is a class attributes.
    salary = 150000

    def __init__(self, name, salary, language): # dunder method which is automatically called.
        self.name = name
        self.salary = salary
        self.language = language
        print("I am Creating an Object.")

    def getinfo(self):
        print(f"The language is {self.language}. The Salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

Aniket = Employee("Aniket", 2900000, "JS")
Aniket.name="Aniket"
print(Aniket.name, Aniket.salary, Aniket.language)

#rohan = Employee()