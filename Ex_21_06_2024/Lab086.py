t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(set(t)) # {'for', 'TheTestingAcademy'}

set1 = {1, 2, 3}
set2 = {4, 5, 6}

set3 = set1.union(set2)
print(set3)

set4 = {1, 2, 3, 4, 5}
set5 = {4, 5, 6, 7, 8}

set6 = set4.intersection(set5)
print(set6)

set7 = set4.difference(set5)
print(set7)

set8 = set5.difference(set4)
print(set8)