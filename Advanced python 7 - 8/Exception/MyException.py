#Creating Userdefined Exception Class
class MyException(RuntimeError):
    def __init__(self,age):
        self.age = age

    @staticmethod
    def sample():
        print("I am Sample from MyException")

    def show(self):
        print("I am show from MyException")

   
#Using Userdefined Exception Class in function
def validate_age():
    user_age  = int(input("Enter age"))
    if(user_age < 0):
        raise MyException("Invalid Age")
    else:
        print("Valid Age")

#Handling the Exception
try:
    validate_age()
except MyException as my:
    print(my)
    my.sample()
    my.show()
else:
    print("I am Else")
finally:
    print("Thanks")


    








