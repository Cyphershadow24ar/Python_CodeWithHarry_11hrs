#Write a Class ‘Train’ which has methods to book a ticket, 
# get status (no of seats) and get fare information of 
# train running under Indian Railways.

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}.")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running On time.")

    def getfare(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}.")

t = Train(12802)
t.book("Jsr", "Bbsr" )
t.getstatus()
t.getfare("Jsr", "Bbsr" )