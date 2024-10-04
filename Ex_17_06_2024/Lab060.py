# *args --> you can add any number of arguments
# print("name1", "name2", "name3")

# def sum_of_three_numbers(a,b,c):
#     return a+b+c
#
# result = sum_of_three_numbers(2, 3, 4)
# print(result)

def sum_of_three_numbers(a=1,b=1,c=1):
    return a+b+c

result1 = sum_of_three_numbers()
result2 = sum_of_three_numbers(2, 3)
result3 = sum_of_three_numbers(2, 3, 4)
result4 = sum_of_three_numbers(a=10, b=20, c=30)
result5 = sum_of_three_numbers(b=15, a=20, c=30)
print(result1, result2, result3, result4, result5)
