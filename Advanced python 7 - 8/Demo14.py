import calendar as cal


# Program to display no of day's in a month

for x in range(1,13):
    print("Month ",x,cal.mdays[x])

#----------------------------------
# Program to check given year is leap year or not

year = int(input("enter a year "))
result = cal.isleap(year)
print(result)

#-----------------------------

# Program to Print calendar
year = int(input("Enter Year : "))
month = int(input("Enter Month : "))

print(cal.month(year,month))

#------------------------------
# Program to Print calendar from Given Day

year = int(input("Enter Year : "))
month = int(input("Enter Month : "))

tcal = cal.TextCalendar(cal.FRIDAY)

print(tcal.formatmonth(year,month))








