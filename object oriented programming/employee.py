class Employee:
    company="luminar technolab"
    def setvalue(self,name,empid,desig,salary):
        self.name=name
        self.empid=empid
        self.desig=desig
        self.salary=salary

    def printval(self):
        print(self.name)
        print(self.empid)
        print(self.desig)
        print(self.desig)
        print(self.salary)
        print(Employee.company)
emp=Employee()
emp.setvalue("Arjun",1001,"Manager",20000)
emp.printval()