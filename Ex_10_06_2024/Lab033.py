# Program - Calculate the area of circle
# input -> radius
# output -> area
import math

# Identify data types
# input -> int or float? -> float
# output -> float

# Core login --> pi * r * r
# use math.pi to get value of pi or use 3.14

radius = float(input("Enter the radis : \n"))
area = math.pi * radius * radius   #
area2 = math.pi * math.pow(radius, 2)
area3 = math.pi * (radius**2)

print(area)
print(area2)
print(area3)