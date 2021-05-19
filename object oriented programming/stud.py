class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return self.name
f = open("stud", "r")
for lines in f:
    words = lines.rstrip("\n ").split(",")
    name=words[0]
    age=words[1]
    stud=Student(name,age)
    print(stud)




# class Student:
#     def __str__(self):
#         f = open("stud", "r")
#         for lines in f:
#             self.words = lines.rstrip("\n ").split(",")
#             for i in self.words:
#               return str(i)
#
# stud=Student()
# print(stud)
#
#
#
