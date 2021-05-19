class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
pe=Person("anu",25,"female")
pe.printval()