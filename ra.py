
# A simple program to calcute number of seconds in a typical year

import pyfiglet
font = pyfiglet.figlet_format("Let's Calculate Seconds in a Year")
print(font)

thisYear = int(input("How many days are in this year: "))

daysYear = 365
daysLeapYear = 366

hoursDay = 24
minutesHour = 60
secondsMinute = 60

normalYear = daysYear * hoursDay * minutesHour * secondsMinute
leapYear = daysLeapYear * hoursDay * minutesHour * secondsMinute

if thisYear == 365:
    print("The seconds in this year are: ", normalYear)
elif thisYear == 366:
    print("The seconds in this year are: ", leapYear)

else :
    print("The days of year entered not valid. We can only have 366 for a leap year and 365  for a normal year ")

print("Thank you for using this program")


