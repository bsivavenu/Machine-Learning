class A:
    def afun(self):
        print(" I am A class Function")

class B:
    def bfun(self):
        print(" I am B class Function")

class C(A,B):
    def cfun(self):
        print(" I am C class Function")
#---------------------------------
c1 = C()
# by using c1 we can call C,A,B class Members
c1.afun()
c1.bfun()
c1.cfun()
#-------------------------
b1 = B()
# by using b1 we can call B class Members only
# b1.afun() Error
b1.bfun()










