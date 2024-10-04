# Tuple - Collection of items
# Tuple is immutable

my_list = [1, 2, 3, 4, 5]
print(id(my_list))
my_list[0] = 21 # List is Mutable
print(my_list)
print(id(my_list))

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(id(my_tuple))
# my_tuple[0] = 21 # Not possible with tuple