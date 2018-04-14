class A:
    def fun(self,name="dummy",age=0):
        print("I am fun")
        print(name)
        print(age)

#------------------------------------
a1 = A()
a1.fun()
a1.fun("Ravi")
a1.fun("kumar",23)
a1.fun(age=23)
a1.fun(age=1020120,name="Krishna")
