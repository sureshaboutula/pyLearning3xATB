# For loop
# for counter in range(1, 100):  # 0 to 99
#     print(counter)
#
# for counter in range(1, 101):  # 1 to 100
#     print(counter)
#
# for counter in range(1, 100, 2):  # 1, 3, 5 to 99 --> All the odd numbers
#     print(counter)
#
# for counter in range(0, 101, 2):  # 0, 2, 4 to 100 --> All the even numbers
#     print(counter)

# break ---> will kick you out of the loop based on the condition

for counter in range(1, 101):
    print(counter)
    if counter == 5:
        break ### control will stop the loop when counter is 5

print("Out of the loop")