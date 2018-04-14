file_name = input("File Name : ")
try:
    f = open(file_name,"r")
except:
    print("File Not Found")
else:
    #print(type(f))
    print(f.read())
       
