# Recursion - Programming technique where a function call itself inorder to solve a problem

# Key concepts
# 1. Base Case
# 2. Recursive Case

# Factorial
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)

print(factorial(5))