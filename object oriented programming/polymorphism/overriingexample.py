class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):
    def setval(self,rollno,dep,mark):
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
        print(self.rollno)
        print(self.dep)
        print(self.mark)
stud=Student()
stud.setval(25,"bca",50)

