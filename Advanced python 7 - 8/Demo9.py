class Employee:
    comp_name = "sathya"   

    def __init__(self,fname="dummy",lname="dummy"):
        self.emp_fname = fname
        self.emp_lname = lname

    def display(self):
        print(self.emp_fname)
        print(self.emp_lname)

#-------------------------------
Employee().display() #output : dummy dummy

Employee("Ravi").display()#output : Ravi dummy

# I Want to pass kumar as last name

Employee("kumar").display()#output : kumar dummy

Employee(lname="kumar").display()#output: dummy kumar
         
lname = input("Enter the Last Name")
fname = input("Enter the First Name")

Employee(lname=lname,fname=fname).display()






