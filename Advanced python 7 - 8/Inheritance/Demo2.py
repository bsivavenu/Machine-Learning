class A:
    def __init__(self):
        print("I am Default Const of A")

    def display(self):
        print(" I am display of A Class")

class B(A):    
    def __init__(self):        
        print("I am Default Const of B")

    def show(self):
        print(" I am show of B Class")


#-----------------------
b1 = B()# B Class Const is Called
b1.show() 
b1.display()








        
