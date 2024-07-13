# Multiple conditions - Use Match case

# numbers = int(input("Enter a Number \n"))
# match numbers:
#     case 1:
#         print("Hello this is 1")
#     case 2:
#         print("Hello this is 2")
#     case 3:
#         print("Hello this is 3")
#     case 4:
#         print("Hello this is 4")
#     case 5:
#         print("Hello this is 5")
#     case 6:
#         print("Hello this is 6")
#     case _:
#         print("No idea")


# String Example for match case

# name = input("Enter the Name \n")
# match name:
#     case "Suresh":
#         print("Hi Suresh")
#     case "Kirti":
#         print("Hello Kirti")
#     case _:
#         print("you are not a human")

# Real time example
browser = input("Enter the Name of the browser \n")
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code executed")
    case "firefox":
        print("Firefox code executed")
    case _:
        print("no browser found")