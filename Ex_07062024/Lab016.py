# Take 2 intiger numbers from the user and add them
# We need to use input function

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# type conversion - str -> int
result1 = num1 + num2
result2 = int(num1) + int(num2)
print(result1)
print(result2)

# + on int -> sum operation
# + on str -> concat

# int to str -> str()
# str to int -> int()

print(type(num1))
print(type(num2))