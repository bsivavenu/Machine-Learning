class Bank:
    i_rate = 3.25
    
    def __init__(self,bal=0.0):
        self.balance = bal
        
    def deposit(self,amount):
        self.balance += amount

    def showbalance(self):
        print(self.balance)


class ICICI(Bank):
    def showInt(self):
        print(Bank.i_rate)
        

#-----------------------------
i1 = ICICI();
i1.deposit(1000)
i1.showbalance()
i1.showInt()
