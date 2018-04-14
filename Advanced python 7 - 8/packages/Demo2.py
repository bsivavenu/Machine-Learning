# Call A class from  A module which is in
# example package

from example.A import A

a1 = A()
a1.fun1()
print(A.comp_name)
#   or
print(a1.comp_name)
