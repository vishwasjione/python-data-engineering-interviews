l1 = [4, 3, 0, 4, 3, 9, 2, 4]

# 1st method
print(l1.count(4))

# 2nd method --best method

# sort list
l1.sort()
print(l1)
# finding first occurrences of element

indx = l1.index(4)
print(indx)

l2 = l1[indx:]
print(l2)
cnt = 0
for v in l2:
    if v == 4:
        cnt += 1
    else:
        break  # the list is sorted so the moment it is not 4 we can come out
print(cnt)

# 3rd method

l1 = [4, 3, 0, 4, 3, 9, 2, 4]

check4 = lambda x: x == 4
# check4 = lambda x: 1 if x == 4 else 0

l2 =  filter(check4,l1)
# l2 =  map(check4,l1)

print((list(l2)))

# still the 2nd method is best one