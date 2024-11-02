class Employee:
    language = "py" # This is a class attributes.
    salary = 150000

Aniket = Employee()
Aniket.name = "Aniket" # This is an object / instance attribute
print(Aniket.name, Aniket.language, Aniket.salary)

rohan = Employee()
rohan.name = "rohan roro robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is object/instance attribute and salary and language 
# are class attributes as they directly belong to the class.