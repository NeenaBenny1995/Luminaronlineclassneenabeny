class Bank:
    bankname="SBI"
    def register(self,name,age,adress,phone):
        self.name=name
        self.age=age
        self.address=adress
        self.phone=phone
        self.minbal=5000
        self.balance=self.minbal
        print(self.name)
        print(self.age)
        print(self.address)
        print(self.phone)
        print(self.minbal)
        print(Bank.bankname)
        print()
    def deposit(self,amount):
        self.amount=amount
        self.balance = self.amount + self.minbal
        print("account credited with",self.amount)
        print()
        print("your availabile balance",self.balance)
        print()


    def withdraw(self,withamount):
        self.withamount=withamount
        if self.withamount>self.balance:
            print("unsufficientbalance")
        else:
            print("account debitted with ",self.withamount)
            print()
            self.balance-=self.withamount
            print("your availabile balance ",self.balance)
ban=Bank()
ban.register("Neena",25,"konattu",9495302779)
ban.deposit(5000)
ban.withdraw(2000)

ban2=Bank()
ban2.register("sibin",28,"aattinedath",326555555)
ban2.deposit(2000)
ban2.withdraw(10000)



