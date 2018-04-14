class A:
    def __init__(self,no=0):
        print("I am Const of A")
        self.no = no

    def display(self):
        print(" I am display of A Class")
        print(self.no)

class B(A):    
    def __init__(self,name="dummy"):
        print("I am Const of B")
        self.name = name

    def show(self):
        print(" I am show of B Class")
        print(self.name)

#-----------------------------------
b1 = B()
b1.show()
b1.display() # Error  because no variable is not init













