#this is multiplication
for j in range(1,11):
    for i in range(1,11):
        print(j*i, end ="\t")
num = int(input("multiplication table of:"))
for i in range(1,11):
    print(num,'*',i,'=',num*i)        