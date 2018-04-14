class ICICI:
    #static variable
    i_rate = 5.25
    balance = 0

    @staticmethod
    def showIR():#no self
        print(ICICI.i_rate)#called with class name
   
    def deposit(self,amount):#instant method with self        
        self.balance = self.balance + amount  
    
    def showBalance(self):#instant method with self
        print("Balance = ",self.balance)


#ICICI.showIR()
