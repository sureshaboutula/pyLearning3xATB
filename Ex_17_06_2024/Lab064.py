# Leap Year Checker

def is_leap_year(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        return True
    else:
        return False

year = int(input("Enter the year to check whether it is leap year or not :"))
result = is_leap_year(year)
print(f"is {year} leap year?: {result}")