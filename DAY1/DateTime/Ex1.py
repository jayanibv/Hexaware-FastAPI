from datetime import datetime

now=datetime.now()
print("Current date and time: ", now)
print(" Year: ", now.year)
print(" Month: ", now.month)
print(" Day: ", now.day)
print(" Hour: ", now.hour)
print(" Minute: ", now.minute)
print(" Second: ", now.second)
print(" Microsecond: ", now.microsecond)

print("Date Formatting: ")
print("Formatted time: ", now.strftime("%H:%M:%S"))
print("Formatted date: ", now.strftime("%Y-%m-%d"))
print("Formatted date and time: ", now.strftime("%B %d %Y"))
print("Formatted date and time: ", now.strftime("%d/%m/%Y"))
print ("IST Time: ", now.strftime("%I:%M %p"))
print(now.strftime("%A %B %d %Y"))

'''
B-Weekday, Month, Day, Year
A-Weekday, Month, Day, Year
H-Hour, Minute, Second, Microsecond
I-Hour, Minute, Second, Microsecond
d-Day
m-Month
M-Month
difference between m and M is that m is 01-12 and M is 1-12
y-Year
Y-Year
p-AM/PM
'''
