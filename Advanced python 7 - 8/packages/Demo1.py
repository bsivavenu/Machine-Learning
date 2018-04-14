# Using package in other module
# Note: This module is out side the package
# In This mobule we are using "sample" module from "example" package

#from example import sample

#sample.one()
#sample.two()
#print(sample.name)
#---------------------------

# In this example we are calling one
# function from module

from example.sample import one

one()



















