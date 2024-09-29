def print_argument(*args):
    print(args)
    for i in args:
        print(i, end="\n")

print_argument("Suresh", "Ramesh", "Naresh")
# *args is a list

a = ["Suresh", "Ramesh", "Naresh"]
for i in a:
    print(i, end="\n")