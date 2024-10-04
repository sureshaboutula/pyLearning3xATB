# Functions
# Block of code - which can be executed or reused

# Define function
# Call function

# Built in Functions --> present in builtins.py file (Python 3 setup)
# Which are created by the Python contributors
#result = max(2, 3)

# User defined functions
    #1. They can return something
    #2. They Can't return - Non return
    #3. They have parameters/arguments
    #4. They don't have parameters/arguments

# No return type and no parameters
# def say_hello():
#     print("Hello")
#
# result1 = say_hello()
# print(result1)
#
# # No return type and with Arguments
# def say_hello_arg(name):
#     print("Hello", name)
#
# say_hello_arg("Suresh")
# say_hello_arg("Pramod")
#
# print(say_hello_arg("Suresh"))

# No Return Type and Default Argument
# def say_hello_arg_default(name="Suresh"):
#     print("Hello", name)
#
# # say_hello_arg_default()
# # say_hello_arg_default("Tejo")
# result1 = say_hello_arg_default()
# print(result1)
# result2 = say_hello_arg_default("Tejo")
# print(result2)

# Return Type and with Arguments
def sum_number_argument_return(a, b):
    return a + b

result = sum_number_argument_return(3, 8)
print(result)
