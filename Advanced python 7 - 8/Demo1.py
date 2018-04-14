class Employee:

    #static variable
    company_name = "Sathya"
       
    #instance Function
    #(Assigning values to instance variables)
    def assign(self,name,sal):
        self.emp_name = name
        self.emp_sal = sal
        
    #instance Function
    #Displaying values of instance variables)
    def display(self):
        print(Employee.company_name)
        print(self.emp_name)
        print(self.emp_sal)

#-------------------------------
e2 = Employee()
e2.assign("Ravi",125000.00)
e2.display()





