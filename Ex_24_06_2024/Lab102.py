# Leetcode program - Sum of digits

#number = 12345
# sum of digits = 1+2+3+4+5

def sum_of_digits(number):
    if number < 10:
        return number
    else:
        # q = number%10
        # number = number//10
        # sum = q + sum_of_digits(number)
        return number%10 + sum_of_digits(number//10)

print(sum_of_digits(199))

# Without recursion:
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        sum_digits = sum_digits + number%10
        number = number // 10
    return sum_digits

print(sum_of_digits(12345))
