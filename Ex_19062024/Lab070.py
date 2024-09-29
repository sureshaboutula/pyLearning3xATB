numbers = [1, 2, 3] # Collection of items

def do_something(list):
    list.append(4)
    list[0] = 15
    return list

print(do_something(numbers))