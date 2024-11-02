class Employee:
    language = "py" # This is a class attributes.
    salary = 150000

Aniket = Employee()
Aniket.language = "JS" # This is an object / instance attribute
print(Aniket.language, Aniket.salary)

# Note: Instance attributes, 
# take preference over class attributes during assignment & retrieval.