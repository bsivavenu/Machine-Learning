 
no1 = int(input("Enter 1st No :"))
no2 = int(input("Enter 2nd No :"))

try:
    print("Div = ",(no1/no2))
except ZeroDivisionError:
    print("Dont Div By Zero(0)")
else:
    print("Else Block")

print("Thanks")
