class Person:
    def setvalue(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
pe=Person()
pe.setvalue("anu",25,"female")
pe.printval()
# class Vehicle:
#     def varients(self,type):
#         self.type=type
#         print(self.type)
# veh=Vehicle()
# veh.varients("white colour benz")