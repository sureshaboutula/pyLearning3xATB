# ✅ #4. Fibonaci series
# 0,0+1, 0+1+1,
# n = 7
# 0, 1, 2, 3, 5, 8, 13


length = int(input("Enter the length of fibonacci series : "))
num1 = 0
num2 = 1

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