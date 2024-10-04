# class Calc:
#
#     def __int__(self): # Does not serve the actual purpose here
#         print("Hello DC")
#     def sum(self, a, b):
#         return a + b
#     def sub(self, a, b):
#         return a - b
#     def mul(self, a, b):
#         return a * b
#     def div(self, a, b):
#         return a / b
#
# object_ref = Calc()
# addition = object_ref.sum(3, 4)
# print(addition)
# subtraction = object_ref.sub(8, 4)
# print(subtraction)
# multiplication = object_ref.mul(3, 4)
# print(multiplication)
# division = object_ref.div(12, 4)
# print(division)

# Rewrite the above code with Constructor
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

object_ref = Calculator(3, 4)
addition = object_ref.sum()
print(addition)


