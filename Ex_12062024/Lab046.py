# Write a program that calculates and displays the letter
# given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
# input - score - 89
# output - B

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Take input -> Integer
score = int(input("Enter the score \n"))

# Calculate output -> string -> A, B, C, D or F

# score >=90 and score <= 100 --> A
# score >=80 and score <= 89 --> B
# score >=70 and score <= 79 --> C
# score >=60 and score <= 69 --> D
# score >=0 and score <= 59 --> F
# any other value > 100 or < 0 --> Invalid

if score >= 90 and score <= 100:
    print("Grade is A")
elif score >= 80 and score <= 89:
    print("Grade is B")
elif score >= 70 and score <= 79:
    print("Grade is C")
elif score >= 60 and score <= 69:
    print("Grade is D")
elif score >= 0 and score <= 59:
    print("Grade is F")
else:
    print("Invalid score")