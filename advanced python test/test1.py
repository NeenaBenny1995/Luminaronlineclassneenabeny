##Create a child class Bus that will inherit all of the variables and methods of Vehicle class?
class Vehicle:
    def __init__(self,number,type):
        self.type=type
        self.number=number
    def printval(self):
        print(self.type)
        print(self.number)
class Bus(Vehicle):
    def __init__(self,busname,buscolor,number,type):
        super().__init__(number,type)
        self.busname=busname
        self.buscolor=buscolor
        print(self.busname)
        print(self.buscolor)
bu=Bus("TVS","blue","KL 07 JH 5252","four wheeler")
bu.printval()
