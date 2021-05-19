class Parent:
    def m1(self):
        print("inside parent class")
class Child:
    def m2(self):
        print("inside child class")
class  Subchild(Child,Parent):
    def m3(self):
        print("inside subclass")

sub=Subchild()
sub.m1()
sub.m2()
sub.m3()