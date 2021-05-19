class Student:
    college="SNGCE"
    def setvalue(self,name,rollnumber,department,sub):
        self.name=name
        self.rollnumber=rollnumber
        self.department=department
        self.sub=sub
    def printval(self):
        print(self.name)
        print(self.rollnumber)
        print(self.department)
        print(self.sub)
        print(Student.college)
        print()
stud=Student()
stud.setvalue("anju",23,"Civil","Maths")
stud.printval()


stud1=Student()
stud1.setvalue("anu",21,"Civil","physics")
stud1.printval()