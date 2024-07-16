#Write a Python program to check whether the given year is leap year or not.

def leap_year(year):
    if ((year%4==0) or (year%100 != 0) and (year%400 == 0)):
        print("The entered year ",year," is a leap year")
    else:
        print("The entered year ",year," is not a leap year")
        
        
leap_year(2024)
leap_year(2020)
leap_year(2021)
leap_year(2012)