#Leap year Checker 
#determine if a year is A LEAP year.(leap years is divisible by 4, but not by 100 unless also divisible by 400).

year = 2028

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, " is a leap year")
else:
    print(year, " is NOT a leap year")    
