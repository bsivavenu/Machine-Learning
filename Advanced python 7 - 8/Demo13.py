class One:
    def maths(self,no1,no2):
        print("Add = ",(no1+no2))
        print("Sub = ",(no1-no2))
              
class Two(One):
    def maths(self,no1,no2):
        super().maths(no1,no2)
        print("Mul = ",(no1*no2))
        print("Div = ",(no1/no2))
        
class Three(Two):
    def maths(self,no1,no2):
        super().maths(no1,no2)
        print("Mod = ",(no1%no2))

#--------------------

print("Please Select Your Class")
print("1) 1st Class :")
print("2) 2nd Class :")
print("3) 3rd Class :")
no = int(input())

#while no not in [1,2,3]:
if(no == 1):
    a = One()   
elif (no == 2):
    a = Two()    
elif(no == 3):
    a = Three()    
else:
    print("Select From Given Options")
    
no1 = float(input("Enter 1st No : "))
no2 = float(input("Enter 2nd No : "))



a.maths(no1,no2)









        
