# ✅ 1. Leap Year Checker:
# Create a program that determines whether a given year is a leap year.
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#
# Use an if-else statement to make this determination.


year = int(input("Enter the year to check whether it is leap year or not :"))

# Logic to verify the given year is leap year

# condition 1 : year is divisible by 4 and not divigible 100
# condition 2: year is divisible by 4 and divisible by 100 and divisible by 400
# condition 3: year is not divisible by 4 -> Not a leap year

if year%4 == 0 and year%100 != 0:
    print(f"Given year {year} is a leap year")
elif year%4 == 0 and year%100 == 0 and year%400 == 0:
    print(f"Given year {year} is a leap year")
else:
    print(f"Given year {year} is not a leap year")