class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):
    def studdet(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno)
        print(self.mark)
class Subchild:
    def det(self,extracarricular):
        self.extracarricular=extracarricular
        print(self.extracarricular)
class School(Person,Subchild):
    def details(self,schoolname,place):
        self.schoolname=schoolname
        self.place=place
        print(self.schoolname)
        print(self.place)
class College(Student):
    def coldetails(self,colname,colplace):
        self.colname=colname
        self.colplace=colplace
        print(self.colname)
        print(self.colplace)
col=College()
col.setval("Anju",21,"female")
col.studdet(24,500)
col.coldetails("st.george","kadayirippu")
print()
stud=Student()
stud.setval("Arjun",20,"male")
stud.studdet(13,450)
print()

sch=School()
sch.setval("Ammu",20,"female")
sch.details("Ghss poothrikka","poothrikka")
sch.det("dance")




