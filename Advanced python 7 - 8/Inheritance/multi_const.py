class A:
    def __init__(self):
        super().__init__()
        print("I am default const of A")
        
   
class B(A):
    def __init__(self):
        super().__init__() # calling super class const
        print("I am default Const of B")       
  

class C(B):
    def __init__(self):
        super().__init__() # calling super class const
        print("I am default Const of C")



#----------
C()
  
