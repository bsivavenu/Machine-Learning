class A:
    def afun(self):
        print(" I am A class Function")

class B(A):
    def bfun(self):
        print(" I am B class Function")

#---------------------        

b1 = B()

# by using b1 we can call
# B class members and A class Members


b1.bfun()
b1.afun()



