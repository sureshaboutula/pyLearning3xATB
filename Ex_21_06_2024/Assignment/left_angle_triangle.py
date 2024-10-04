#Left Triangle Star Pattern

# n = int(input("Enter the number : "))
#
# for i in range(n,1,-1):
#     for j in range(1,i+1):
#         print("* ", end="")
#     print("")


def left_triangle_star_patter(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

left_triangle_star_patter(9)