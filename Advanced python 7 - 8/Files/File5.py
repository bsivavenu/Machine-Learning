# Read all lines without using functions
# we are reading in line by line format
#=======================================

file_name = input("Enter File Name : ")
try:
    f = open(file_name)

    for x in f:
        print(x,type(x))
    
except FileNotFoundError :
    print("Invalid File Name ")
finally:
    print("Thanks")
