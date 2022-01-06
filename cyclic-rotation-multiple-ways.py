l1 = [3,4,6,5,9,1]
print(l1)
l2=[]

n=2

# 1st solution long method
for i in range(n):
    l2.append(l1[len(l1)-1])
    for j in range(len(l1)-1):
        l2.append(l1[j])
    l1=l2
    if i!=(n-1):
        l2=[]

print(l2)

# 2nd solution long method


# 1st solution long method
l1 = [3,4,6,5,9,1]
l3=[]

for i in range(n):
    l3.append(l1[len(l1)-1])
    l3.extend(l1[:-1])
    l1=l3
    if i!=(n-1):
        l3=[]

print(l3)

# 3rd solution - best solution
l1 = [3,4,6,5,9,1]
l4=[None] * len(l1)

for i in range(len(l1)):
    l4[(i+n)%len(l1)]=l1[i]

print(l4)
