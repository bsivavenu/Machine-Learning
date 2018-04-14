class Employee:
    comp_name = "sathya"

    def __init__(self):
        self.name = "ravi"
        self.salary = 125000.00

    def displayDetails(self):
        print(self.name)
        print(self.salary)
        print(Employee.comp_name)

#---------------------

e1 = Employee()
print("1st Object ---",e1)
e1.displayDetails()


e2 = Employee()
print("2nd Object ---",e2)
e2.displayDetails()





