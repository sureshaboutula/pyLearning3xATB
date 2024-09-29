# Factorial
# def factorial_fun(number):
#     factorial = 1
#     for i in range(1, number+1):
#         factorial = factorial * i
#         print(factorial)
#         return factorial
#
# num = int(input("Enter a number to find factorial : "))
# fact_of_num = factorial_fun(num)
# print(f"Factorial of {num} is {fact_of_num}")

def factorial_function(number):
    if number == (0 or 1):
        return 1
    else:
        return number * factorial_function(number-1)

num = int(input("Enter a number to find factorial : "))
fact_of_num = factorial_function(num)
print(f"Factorial of {num} is {fact_of_num}")