class Employee:
    comp_name = "sathya"

    def __init__(self,name,sal):
        self.emp_name = name
        self.emp_salary = sal

    def displayDetails(self):
        print(self.emp_name)
        print(self.emp_salary)
        print(Employee.comp_name)

#-----------------------------------

e1 = Employee("Ravi",10)
e1.displayDetails()

e2 = Employee("Kumar",20)
e2.displayDetails()
