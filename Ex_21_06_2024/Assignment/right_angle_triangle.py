#Right Triangle Star Pattern

# n = int(input("Enter the number : "))
#
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("* ", end="")
#     print("")


def right_triangle_star_patter(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

right_triangle_star_patter(9)