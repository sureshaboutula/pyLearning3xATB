# print(sep="-", "Hi", "Suresh")
# SyntaxError: positional argument follows keyword argument
# end, sep and File=None should be after arguments

############################################################

print("I am a Good Person")
print("I am a Bad Person")

# Modify above code to show them in same line with "_" separator
print("I am a Good Person", end="_")
print("I am a Bad Person")

# Modify above code to show them in same line with space separator
print("I am a Good Person", end=" ")
print("I am a Bad Person")

# Modify above code to show them in same line with tab space separator
print("I am a Good Person", end="\t")
print("I am a Bad Person")