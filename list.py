l1=[4,6,7,8,9,8,9,8,9,9,1,1,1,1,1]
l2=[]

# manual way
for value in l1:
    if value not in l2:
        l2.append(value)
print(l2)

# using set
l3=set(l1)
print(list(l3))

# max repeatance
cntdct={}
for value in l1:
    if value not in cntdct:
        cntdct[value]=1
    else:
        cntdct[value] += 1

print(cntdct)
#print(max(cntdct))  # key with max value
#print(list(cntdct.values()))

# (1, 5)
# (4, 1)
# (6, 1)
# (7, 1)
# (8, 3)
# (9, 4)

# manually finding max value from dictionary
# sort by value
for i in sorted(cntdct.items(),key=lambda x:x[1]):  # x[1] is value
    print(i)
# sort by key
for i in sorted(cntdct.items(),key=lambda x:x[0]): # x[0] is key
    print(i)

sorted_dct = sorted(cntdct.items(),key=lambda x:x[0])
print(dict(sorted_dct))

print ("----------------------------")
print(cntdct)
newdict={}
for i in sorted(cntdct.items(),key=lambda x:x[0]):  # x[1] is value
    newdict[i[0]]=i[1]
print(newdict)

