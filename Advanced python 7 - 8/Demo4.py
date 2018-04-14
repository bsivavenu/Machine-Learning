class Demo4:
    #static variable
    name = "Sathya"

    @classmethod
    def sample(cls):
        #Calling static variable using class name
        print(Demo4.name)
        #static variable is available for class
        print(cls.name)

    @classmethod
    def sample2(cls):
        Demo4.name = "Sathya Tech"
        print(Demo4.name)
        cls.name = "Sathya Tech AMPT"
        print(cls.name)

#----------------------
print("Before Calling Functions -- ",Demo4.name)
Demo4.sample()# sathya  sathya
Demo4.sample2()        
print("After Calling Functions -- ",Demo4.name)

#---------------------

Demo4().sample()





