# Fibonaci series

def fibonaci_fun(num1, num2, length):
    if length > 2:
        print(num1)
        print(num2)
        for i in range(2, length):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            print(num3)
    elif length == 2:
        print(num1)
        print(num2)
    elif length == 1:
        print(num1)
    else:
        print("Invalid length")

num1 = int(input("Enter first number of the series : "))
num2 = int(input("Enter second number of the series : "))
length = int(input("Enter length of the series : "))

fibonaci_fun(num1, num2, length)
fibonaci_fun(0, 1, 1)