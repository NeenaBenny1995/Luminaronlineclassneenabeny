#tostng method
###only return one string value.if u are added more than one value use string concat

class Animal:
    def __init__(self,name,category):
        self.name=name
        self.category=category
        print(self.name)
        print(self.category)
class Dog(Animal):
    def __init__(self,dogname,dogtype,name,category):
        super().__init__(name,category)
        self.dogname=dogname
        self.dogtype=dogtype
        print(self.dogname)
        print(self.dogtype)

dg=Dog("Toby","Doberman","Dog","pet")


