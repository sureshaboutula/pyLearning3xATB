# ✅ 2. Triangle Classifier:
# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.
# 3 Input
# side 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3


side1 = int(input("Enter the side 1 of the triangle :"))
side2 = int(input("Enter the side 2 of the triangle :"))
side3 = int(input("Enter the side 3 of the triangle :"))

# Check if the triangle is equilateral
if side1 == side2 == side3:
    print("Given lengths belong to a equilateral triangle")
elif side1 == side2 != side3 or side2 == side3 != side1 or side3 == side1 != side2:
    print("Given lengths belong to a isosceles triangle")
else:
    print("Given lengths belong to a scalene triangle")