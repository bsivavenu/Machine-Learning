def createFile():
    file_name = input("Enter File Name : ")
    f = open(file_name,"w")
    print("File Created")
    f.close()

print("1) Create ")
print("2) Open and Read")
print("3) Write ")
option = int(input("Select One Option : "))
if((option>=1) and (option<=4)):
    if(option == 1):
        createFile()
    elif (option == 2):
        file_name = input("Enter File Name :")
        print(open(file_name).read())
    else:
        file_name = input("Enter File Name :")
        f = open(file_name,"a")
        data = input("Enter Some Data to File")
        f.write(data)
        f.close()
        print("Data Written to File")
else:
    print("Select Option From Given Menu Only")


