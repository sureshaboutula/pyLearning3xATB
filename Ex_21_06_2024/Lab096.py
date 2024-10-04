my_dict = {'b':2, 'a':1, 'c':26, 'w':19}
print(my_dict)

for k,v in my_dict.items():
    print(k,v)

# Generally Dict is unordered list

# Dict will not keep the order of insertion
# OrderedDict - It will keep the order of insertion

from collections import OrderedDict 

od = OrderedDict()
od['a'] = 45
od['c'] = 78
od['b'] = 12
od['d'] = 28
print(od)