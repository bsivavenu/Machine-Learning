#Reading 1 line From a File

file_name = input("Enter File Name : ")
try:
    f = open(file_name)
    print(f.readline())
except FileNotFoundError :
    print("Invalid File Name ")
finally:
    print("Thanks")
