import calendar as cal

year = 2025
month = 1

print(cal.month(year,month))

c = cal.TextCalendar(cal.FRIDAY)
str = c.formatmonth(2025,1)
print(str)

print(cal.mdays)
print(cal.isleap(2000))
print(cal.leapdays(1998,2018))
