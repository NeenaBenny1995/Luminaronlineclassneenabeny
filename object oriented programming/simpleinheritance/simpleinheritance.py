class Person:      #parentclass/superclass/
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):#childclass/derivedclass/subclass
    def studval(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def displayval(self):
        print(self.rollno)
        print(self.school)
per=Person()
per.setval("arjun",25,"male")
per.printval()
stud=Student()
stud.studval(21,"luminar")
stud.displayval()
stud.setval("anu",20,"female")
stud.printval()