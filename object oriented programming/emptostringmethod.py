class Employee:
    def empmethod(self,name,id,age,salary):
        self.name=name
        self.id=id
        self.age=age
        self.salary=salary
        print(self.name)
        print(self.id)
        print(self.age)
        print(self.salary)

    def __str__(self):
        return self.name+str(self.id)
emp=Employee()
emp.empmethod("arjun",10002,28,25000)
print("object reference using tostring method::::::",emp)
