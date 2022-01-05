s1 = "hardly any snow season in atlanta"

# sorting logic without any functions

# strings are imutable hence we cannot change in place or create any other temp string
# we will have to convert it to list

l1 = s1.split()

l2 = []
print(l1)

# 1st way long way
for i in range(len(l1) - 1, -1, -1):
    print(i, ' ', l1[i])
    l2.append(l1[i])
print('1st way')
print(l2)

l2 = []

# 2nd way easy way
for i in range(len(l1)):
    value = l1.pop()
    l2.append(value)
print('2nd way')
print(l2)

# 3rd way complex but shortest way
l1 = s1.split()

# 0 first -> -1 last
# 1 second -> -2 second last
# 2 -> -3
# 3 -> -4
# 4 -> -5
# 5 -> -6


for i in range(len(l1) // 2):
    l1[i * -1 - 1], l1[i] = l1[i], l1[i * -1 - 1]
print('3rd way')
print(l1)

# 4th way most optimum way
l1 = s1.split()
l2=l1[::-1]
s2=' '.join(l2)
print(s2)
