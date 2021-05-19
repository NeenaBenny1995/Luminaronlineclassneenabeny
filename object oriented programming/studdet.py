class Student:
    def __init__(self,name,rollno,dep,mark):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
    def __str__(self):
            return (self.name)
f=open("studdet","r")
for lines in f:
    data=lines.rstrip("\n ").split(",")
    name=data[0]
    rollno=data[1]
    dep=data[2]
    m=int(data[3])
    if m > 190:
        stud=Student(name,rollno,dep,m)
        print(stud)
