with open("naveen.txt") as f:
    for line in f:
        print(line)

#----------------------

f = open("naveen.txt","w")
f.write("Hi\n")
f.write("This is Naveen\n")
f.write("From Sathya")
f.close()
