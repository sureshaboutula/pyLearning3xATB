# Dictionary - Key and Value pair
# name : "Suresh"
my_dict = {} # Empty Dict
my_dict2 = {
    "name":"Suresh",
    "age":45,
    "address":"Toronto"
}

print(my_dict2)
print(len(my_dict2))
print(my_dict2["name"])
print(my_dict2["age"])
print(my_dict2["address"])


phone_book = dict(name="Suresh", age=57, address="Toronto")
print(phone_book)
print(len(phone_book))
print(phone_book["name"])
print(phone_book["age"])

phone_book["age"] = 35
print(phone_book)
print(phone_book["age"])

