class A:
    def c(self,name):
        print("i am a",name)
        
class B(A):
    def c(self):
        super().c("Naveen")
        print("i am b")
        
