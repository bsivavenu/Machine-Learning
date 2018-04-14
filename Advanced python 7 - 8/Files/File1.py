file_name = input("Enter File Name : ")
try:
    f = open(file_name,"r")    
except FileNotFoundError as fnfe:
    print("Invalid File Name")
else:
    print(f)
finally:
    print("Thanks")
