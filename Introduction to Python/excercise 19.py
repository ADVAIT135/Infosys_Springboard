# Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def next_15_leap_years(start_year):
    leap_years = []
    year = start_year
    
    while len(leap_years) < 15:
        if is_leap_year(year):
            leap_years.append(year)
        year += 1
    
    return "The list of next 15 leap years for the provided current year",start_year," is ",leap_years

print(next_15_leap_years(2023))
print(next_15_leap_years(2015))
print(next_15_leap_years(2025))
print(next_15_leap_years(2020))