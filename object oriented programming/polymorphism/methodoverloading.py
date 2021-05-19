#currently python dont support method overloading
#same method name different parameters
class Student:
    def setval(self,name,rollno,dep):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        print(self.name)
        print(self.rollno)
        print(self.dep)
class Child(Student):
    def setval(self,sname,sage):
        self.sname=sname
        self.sage=sage
        print(self.sname)
        print(self.sage)
ch=Child()
ch.setval("anu",21,"bca")