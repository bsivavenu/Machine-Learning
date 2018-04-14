class A:
    def afun(self):
        print(" I am A class Function")

class B(A):
    def bfun(self):
        print(" I am B class Function")

class C(A):
    def cfun(self):
        print(" I am C class Function")
#------------------------
c1 = C()
# by using c1 we can call C,A classes members
c1.afun()
# c1.bfun() Error
c1.cfun()
#-------------------------
b1 = B()
# by using b1 we can call B,A classes Members
b1.afun()
b1.bfun()
# b1.cfun() Error











