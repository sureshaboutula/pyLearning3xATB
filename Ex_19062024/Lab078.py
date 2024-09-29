my_list = [1, 2, 3, 4, 5]

# print(my_list*2) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# temp_list = []
# for i in my_list:
#     # temp = i *2
#     # temp_list.append(temp)
#     temp_list.append(i*2)
#
# print(temp_list)

# def double_item(num):
#     return num*2

double_item = lambda num:num*2

# Map()

# Takes each item from the list
# Execute the function on it
# Return the same number of elements(list)

double_list = list(map(double_item, my_list))
print(double_list)


# Final code :
# my_list = [1, 2, 3, 4, 5]
# double_item = lambda num:num*2
# double_list = list(map(double_item, my_list))
# print(double_list)

#Above code can be reduced further
# my_list = [1, 2, 3, 4, 5]
# double_list = list(map(lambda num:num*2, my_list))
# print(double_list)

# Reduce print line
my_list = [1, 2, 3, 4, 5, 6]
print(list(map(lambda num:num*2, my_list)))

# Further reduce
print(list(map(lambda num:num*2, [1, 2, 3, 4, 5, 6])))
