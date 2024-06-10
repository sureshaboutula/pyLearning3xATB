# List - Shopping List
# Milk, Bread, Butter, Poha

# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit

shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(len((shopping_list)))
print(type(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

# Append()
shopping_list.append("curd") # Add one item at the end of the list
print(shopping_list)
# Insert()
shopping_list.insert(1, "jam") # Add item at the required Index
print(shopping_list)
# extend()
shopping_list.extend(["salt", "chips"]) # Add Multiple items at the end
print(shopping_list)
# remove()
shopping_list.remove("bread") # Remove an item
print(shopping_list)
# pop()
print(shopping_list.pop()) # Last item will be removed and returned
# index()
print(shopping_list.index("butter")) # To find an index of an item
# reverse()
shopping_list.reverse()
print(shopping_list)
# sort()
shopping_list.sort()
print(shopping_list)
# count()
count = shopping_list.count("poha")
print(count)
# copy()
new_shop_list = shopping_list.copy()
print(shopping_list)
print(new_shop_list)



# Lists are Mutable

shopping_list[0] = "buttermilk"
print(shopping_list)


# my_list = [1, 2, 3, 4, True, 3.14, "Pramod"]
# print(type(my_list))