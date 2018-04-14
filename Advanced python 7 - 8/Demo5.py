class Demo5:
    #static variable
    name = "sathya"
    
    def sample(self):
        print(Demo5.name)       
        Demo5.name = "Sathya Tech"
        print(Demo5.name)

    def sample2(self):
        print(self.name)
        self.name = "Sathya Tech AMPT"
        print(self.name)
        print(Demo5.name)
        
#--------------
print("Before Calling Function --",Demo5.name)
d1 = Demo5()
d1.sample()
d1.sample2()
print("After Calling Function --",Demo5.name)







