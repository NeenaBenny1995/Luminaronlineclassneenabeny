class Person:
    def personmethod(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name,self.age,self.gender)
class Employee:
    def empmethod(self,empid,company):
        self.empid=empid
        self.company=company
        print(self.empid,self.company)
class Manager(Person,Employee):
    def managermethod(self,salary):
        self.salary=salary
        print(self.salary)
man=Manager()
man.empmethod(1002,"luminar")
man.managermethod(30000)
man.personmethod("Sibin",28,"Male")

