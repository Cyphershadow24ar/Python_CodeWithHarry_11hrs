# Can you change the self-parameter inside a 
# class to something else (say “harry”). 
# Try changing self to “slf” or “harry” and 
# see the effects.

# NOTE: Answer -> Replacing 'self to 'slf' doesn't change anything & also change 'Harry' it doesn't effects the outputs.
from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}.")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running On time.")

    def getfare(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}.")

t = Train(12802)
t.book("Jsr", "Bbsr" )
t.getstatus()
t.getfare("Jsr", "Bbsr" )