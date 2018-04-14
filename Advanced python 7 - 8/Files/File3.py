# WAP to read only given no of char's
# from a file

file_name = input("Enter File Name : ")
try:
    f = open(file_name)
    no = int(input("Enter no of char's : "))
    print(f.read(no))
except FileNotFoundError :
    print("Invalid File Name ")
finally:
    print("Thanks")
