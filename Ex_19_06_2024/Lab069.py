def outer_function():
    var1 = 30
    def inner_function():
        print(var1)

    inner_function() # Inner function should be called within the outer function

outer_function()

# def outer_function():
#     var1 = 30
#     def inner_function():
#         print(var1)
#
# inner_function() # Error -> Inner function should be called within the outer function
#
# outer_function()

# def outer_function():
#     var1 = 30
#     def inner_function():
#         print(var1)
#
# outer_function() # This wont print var1 as inner function is not called