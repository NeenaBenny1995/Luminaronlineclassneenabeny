class Person:
    def setvalue(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def empsetvalue(self,empid,salary,companyname):
        self.empid=empid
        self.salary=salary
        self.companyname=companyname
    def empdisplayval(self):
        print(self.empid)
        print(self.salary)
        print(self.companyname)
pe=Person()
pe.setvalue("anu",25,"female")
pe.printval()
print()

emp=Employee()
emp.empsetvalue(1001,20000,"luminar")
emp.empdisplayval()
emp.setvalue("sibin",28,"male")
emp.printval()