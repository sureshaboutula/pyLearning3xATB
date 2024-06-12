# Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8

number = int(input("Enter the number to calculate square and cube :"))

print(f"Square value of the given number is {number * number} and Cube value of the given number is {number ** 3}")

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

print(f"{num1} is greater than {num2}" if num1 > num2 else f"{num2} is greater than {num1} " if num1 < num2 else f"{num1} and {num2} are equal")