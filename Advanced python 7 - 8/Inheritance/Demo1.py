class A:
    def sample(self):
        print("I am Sample of A Class")

class B(A): #class B inheriting Class A
    def display(self):
        print("I am dislay of B Class")

#----------------------------
a1 = A()
a1.sample()
# a1.display() Error

b1 = B()
b1.display()
b1.sample()







