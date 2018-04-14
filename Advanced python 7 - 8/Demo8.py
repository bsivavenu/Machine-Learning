class Employee:
    comp_name = "sathya"   

    def __init__(self,name="dummy",sal=0.0):
        self.emp_name = name
        self.emp_salary = sal
        return None

    def displayDetails(self):
        print(self.emp_name)
        print(self.emp_salary)
        print(Employee.comp_name)
#--------------------------------
e1 = Employee()
e1.displayDetails()

e2 = Employee("Krishna",125000.00)
e2.displayDetails()

e3 = Employee("Naveen")
e3.displayDetails()




        
