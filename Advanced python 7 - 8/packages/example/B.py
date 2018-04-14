from A import A 

class B(A):
    def fun2(self):
        super().fun1(no=111,name="ravi")
        print("I am Fun2 From Class B")


