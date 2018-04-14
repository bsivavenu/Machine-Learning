class A:
    def __init__(self):
        super().__init__()
        print("I am Const of A")

    def one(self):
        print("I am from class A")

    def one(self,idno=10,name="ravi"):
        print(idno)
        print(name)          

class B(A):    
    def __init__(self):
        super().__init__()
        print("I am Const of B")

    def one(self):
        super().one()
        print("I am from class B")
        

#-----------------------------
a = A()
a.one()
