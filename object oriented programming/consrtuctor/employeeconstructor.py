class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.salary)
emp=Employee("Arjun",28,10000)
emp.printval()