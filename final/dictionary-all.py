
dict1={"newyork":100,"chicago":200}

# Sorting
sorted_dict1 = sorted(dict1.items(),key=lambda x:x[0])
print(dict(sorted_dict1))

sorted_dict1 = sorted(dict1.items(),key=lambda x:x[1])
print(dict(sorted_dict1))

# checking if a key exists in dict

l1=["newyork","chicago","atlnata","detroit"]

# checking if a key exists in dict1
for value in l1:
    if value not in dict1:  # checking if a key exists in dict1
        dict1[value]=200

print(dict1)

#dict1.items()
#dict1.values()
#dict1.keys()

# comprehansion in dictionary
dictcounts={'a':2,'b':3,'c':7}
dictcountsnoduplicates = {(a, b) for (a, b) in dictcounts.items() if b > 3}
print(dictcountsnoduplicates)
