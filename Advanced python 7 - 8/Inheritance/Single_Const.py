class A:
    def __init__(self):
        print("I am default const of A")
        
   
class B(A):
    def __init__(self):
        super().__init__() # calling super class const
        print("I am default Const of B")       
  
#---------------------        
b1 = B()

