class Demo2:
    @staticmethod #decorator
    def sample1():
        print("I am Static Method")

    @classmethod #decorator
    def sample2(cls):
        print(" I am Class method",cls)


    def sample3(self): # instance method
        print(" I am Instance Method",self)

#-----------------------
#Calling Static Method
Demo2.sample1()

#Calling Class Method
Demo2.sample2()

#Calling Instance Method using Object
Demo2().sample3()

#Calling Instance Method using Object ref variable
d1 = Demo2()
d1.sample3()








