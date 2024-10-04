# map

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def doube_num(num):
    return num*2

doubled_numbers = map(doube_num, numbers)
print(list(doubled_numbers))

# Map gives same number of items as the actual list
# Filter gives less number of items as compared actual list
# Function should return true of flse to use it in Filter function

def even_giver(num):
    return num%2 == 0

filtered_even_num_list = list(filter(even_giver, numbers))
print(filtered_even_num_list)