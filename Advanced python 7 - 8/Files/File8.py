# WAP to Create a File and Write data to it
# Using Append Mode
#===========================================
file_name = input("Enter File Name : ")
try:
    f = open(file_name,"a")
    data = input("Enter some data to File ")
    f.write(data)
    f.close()
except :
    print("Invalid")
