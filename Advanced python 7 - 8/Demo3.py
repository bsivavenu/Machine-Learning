class Demo3:

    #static variable
    name = "sathya"

    @staticmethod
    def sample1():
        #print(name)  --> Error
        print(Demo3.name)
        Demo3.name = "Sathya Tech"
        print(Demo3.name)

#------------------------
print("Before sample function --",Demo3.name)
Demo3.sample1()
print("After sample function --",Demo3.name)


#calling with Object
Demo3().sample1()










    
