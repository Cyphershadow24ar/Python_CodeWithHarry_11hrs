#Create a class “Programmer” for 
#storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Aniket", 2020000, 800026)
print(p.name,p.salary,p.pin, p.company)
q = Programmer("Quince", 2020000, 800001)
print(q.name,q.salary,q.pin, q.company)
r = Programmer("Riya", 2020000, 800002)
print(r.name,r.salary,r.pin, r.company)
s = Programmer("Sunita", 2020000, 830102)
print(s.name,s.salary,s.pin, s.company)
t = Programmer("Tushar", 2020000, 830107)
print(t.name,t.salary,t.pin, t.company)