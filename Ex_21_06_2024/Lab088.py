t = ("TheTestingAcademy", "for", "TheTestingAcademy.")
sett = set(t)
print(len(t))
print(len(sett))

for i in sett:
    print(i)

set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(len(set1))

set1.remove(5)
print(set1)
print(len(set1))

set1.add(13)
print(set1)
print(len(set1))

set1.pop()
print(set1)
print(len(set1))

