def f1(a, b, c):
    return a + b + c
    print("Hello") # This code will be never executed

print("End")

# result = f1(3, 4, 5)
# result = f1(a=4, b=6, c=9)
result = f1(b=6, a=4, c=9)
print(result)