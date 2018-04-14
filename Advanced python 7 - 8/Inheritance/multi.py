class A:
    def afun(self):
        print(" I am A class Function")

class B(A):
    def bfun(self):
        print(" I am B class Function")

class C(B):
    def cfun(self):
        print(" I am C class Function")

#-------------------
c1 = C()
# by using c1 we can call C,B,A class members
c1.cfun()
c1.bfun()
c1.afun()
#---------------------
b1 = B()
# by usign b1 we can call B,A class Members
b1.bfun()
b1.afun()

           















        
