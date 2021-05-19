class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def printstud(self):
        print(self.rollno)
        print(self.mark)
        print(self.name,self.age)
stud=Student(25,35,"anu",25)
stud.printval()
stud.printstud()
