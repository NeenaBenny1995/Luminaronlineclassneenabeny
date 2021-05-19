class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    # num1=int(input("enter a number"))
    # num2=int(input("enter a number"))
    def addition(self):
        self.result=self.num1+self.num2
        print(self.result)
        return
    def subtraction(self):
        self.result=self.num1 - self.num2
        print(self.result)
        return
    def multi(self):
        self.result=self.num1*self.num2
        print(self.result)
        return
    def div(self):
        self.result=self.num1/self.num2
        print(self.result)
        return
calc=Calculator(20,10)
calc.multi()