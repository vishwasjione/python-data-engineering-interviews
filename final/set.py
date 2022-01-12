abc={}
print(type(abc))

abc={"a":12,"b":30,"c":34}
cde={"a":12,"x":30,"c":34}

# Set is kind of unique keys in a dictionary

set1=set(abc)
set2=set(cde)

fnl1 = set1 - set2  # set minus operation
print(fnl1)
fnl2 = set2 - set1
print(fnl2)
fnl3= set1.union(set2) # union set
print(fnl3)
fnl4= set1.intersection(set2) # intersection
print(fnl4)

# print((cde))