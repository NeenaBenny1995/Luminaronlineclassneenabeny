class Addition:
    def setnum(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def addvalue(self):
        result=self.num1+self.num2
        print(self.num1,"+", self.num2 ,"is" ,result)
add=Addition()
add.setnum(10,20)
add.addvalue()