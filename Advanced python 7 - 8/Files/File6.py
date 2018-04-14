# reading data from file using redlines()
#========================================
file_name = input("Enter File Name : ")
try:
    f = open(file_name)  
    l1 = f.readlines()
    for x in l1:
        print(x)
except FileNotFoundError :
    print("Invalid File Name ")
finally:
    print("Thanks")
