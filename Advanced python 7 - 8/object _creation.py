class Bank:
    name = None
    def assignName(self,bname):
        self.name = bname
        
    def displayName(self):
        print(self.name)
        

#Object Creation
b1 = Bank()
#Calling Function's
b1.displayName() #None
b1.assignName("Kotak")
b1.displayName() #Kotak

#Object Creation
b2 = Bank()
#Calling Function's
b2.assignName("SBI")
b2.displayName()
