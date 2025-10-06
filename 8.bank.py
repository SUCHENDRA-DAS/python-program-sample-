class bankaccount:
    def __init__(self,balance=0):
        self.balance=balance
        print("The Bank Balance : ",self.balance)
    def deposit(self,amount):
        self.balance+=amount
        print("The Bank Balance After Deposit : ",self.balance)
    def withdraw(self,amount):
        if self.balance<amount:
            self.balance-=amount
            print("The Bank Balance After Withdrawing : ",self.balance)
        else:
            print("Insufficient Amount")
class savingaccount(bankaccount):
    def __init__(self,balance=0,interest=0):
        self.interest=interest
        super().__init__(balance)
    def interest():
        interest=self.balance*(self.interest/100)
        self.balance=self.balance+interest
        print("The Bank Balance With Interest : ",self.balance)            
obj=bankaccount(1000)
obj.deposit(500)
obj.withdraw(300)
obj1=savingaccount(1200,5)
obj1.interest()
