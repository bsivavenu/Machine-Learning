#WAP to Print a Simple Calc (+,-,*,/)

no1 = int(input("Enter 1st No :"))
no2 = int(input("Enter 2nd No :"))

print("Sum = ",(no1+no2))
print("Sub = ",(no1-no2))
try:
    print("Div = ",(no1/no2))
except ZeroDivisionError:
    print("Dont Div By Zero(0)")
    
print("Mul = ",(no1*no2))
print("Thanks")
