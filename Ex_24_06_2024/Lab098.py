# Filter in Python
# The filter() function in python is a built-in function
# allows you to filter elements in the list, tuple, set.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Create filter to list even numbers [2, 4, 6, 8, 10]

def is_even(num):
    return num % 2 == 0

def is_greater_than_5(num):
    return num > 5

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

greater_then_5_numbers = filter(is_greater_than_5, numbers)
print(list(greater_then_5_numbers))
