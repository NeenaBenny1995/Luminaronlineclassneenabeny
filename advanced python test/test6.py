class Student:
    def __init__(self,name,rollno,dep,mark):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
    def __str__(self):
            return (self.name+self.rollno+self.dep+str(self.mark))
f=open("stud","r")
mk=[]
for lines in f:
    data=lines.rstrip("\n ").split(",")
    name=data[0]
    rollno=data[1]
    dep=data[2]
    m=int(data[3])
    mk.append(m)
# maximum=max(mk)
# stud=Student(name,rollno,dep,m)
# print(stud)
    if m==max(mk):
           stud=Student(name,rollno,dep,m)
           print(stud)
