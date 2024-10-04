# Operators:

# Assignment Operator
# "=" -> Assign the value from right to left
name = "Suresh"

# Compare operator
 # == is comparison operator

v1 = (1 == True)
v2 = (0 == False)

print(v1)
print(v2)

# Unary Operator -> +, -
age = +65 # + sign can be ignored as the default sign is always +
num = -1
print(age)
print(num)

r = age + num # 65 + (-1) = 64 -> BODMAS -> MATHS
print(r)

# Not operator
is_married = True
print(not is_married)

# Is Operator -> Identity operator
a = 5
b = 6
c = False
print(a is b)

my_list1 = [1, 2, 3]
my_list2 = [1, 2, 3]
print(my_list1 is my_list2) # False. Because location is different