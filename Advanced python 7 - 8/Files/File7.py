# WAP to Create a File and Write data to it
#===========================================
file_name = input("Enter File Name : ")
try:
    f = open(file_name,"w")
    data = input("Enter some data to File ")
    f.write(data)
    f.close()
except :
    print("Invalid")
