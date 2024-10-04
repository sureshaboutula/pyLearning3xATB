suresh_details = {
    "name" : "Suresh",
    "90" : 34.34,
    "isMale" : True,
    "State" : "KA"
}

print(suresh_details.get("name"))
print(suresh_details["name"])
print(suresh_details.values())
print(suresh_details.keys())

my_dict = {'a':1, 'b':2, 'c':3, 'a':95, 'd':95}
print(my_dict)
print(len(my_dict))

# Keys dont accept duplicates
# Values can have duplicate values
print(list(my_dict.keys()))
print(list(my_dict.values()))

for i in list(my_dict.keys()):
    print(i)

for i in list(my_dict.values()):
    print(i)

for i, j in my_dict.items():
    print(i, j)