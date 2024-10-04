# Unpacking of tuple
a, b, c  = (12, 34, 56)

t = (22, 44, 76)
print(t)
# t.append() will not work as tuples are immutable
new_t = t + (46,)
print(new_t)

# Convert to a list
t_list = list(t)
t_list.append(46)
new_t2 = tuple(t_list)
print(new_t2)
