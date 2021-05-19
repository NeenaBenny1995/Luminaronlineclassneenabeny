class Person:
    def setvalue(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Parent(Person):
    def parentsetvalue(self,salary):
        self.salary=salary
        print(self.salary)
class Child(Person):
    def childsetvalue(self,job,place):
        self.job=job
        self.place=place
        print(self.job)
        print(self.place)
class Student(Child):
    def studset(self,rollno):
        self.rollno=rollno
        print(self.rollno)

per=Person()
per.setvalue("neena",26,"female")
par=Parent()
par.setvalue("anu",25,"female")
par.parentsetvalue(25000)
ch=Child()
ch.setvalue("arjun",25,"male")



