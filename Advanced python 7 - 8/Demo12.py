class A:
    def calc(self,no1,no2):
        print(no1,no2,"sum = ",(no1+no2))


class B(A):
    def calc(self,no1,no2):
        A().calc(no1,no2)
        super().calc(no1,no2)
        print(no1,no2,"sub = ",(no1-no2))

#----------------
      
a1 = A()
print("Enter 2 No's")
a1.calc(int(input()),int(input()))

#----------------------------

b1 = B()
print("Enter 2 No's")
b1.calc(int(input()),int(input()))








