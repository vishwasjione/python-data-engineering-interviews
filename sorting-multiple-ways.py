# Sorting a list

l1 = [1, 2, 3, 4, 6, 5]
print(l1)

###### by logic & not using any functions

print("Using logic")
print("**********")

for i in range(len(l1) - 1):
    if l1[i] > l1[i + 1]:
        l1[i + 1], l1[i] = l1[i], l1[i + 1]

# above loop has to be executed at least len(l1)-1 times
# len(l1)-1 times because we are doing l1[i+1] below otherwise it will be index out of error

# list reset
l1 = [1, 2, 3, 4, 6, 5]

for j in range(len(l1) - 1):
    for i in range(len(l1) - 1):
        print("first approach inner-loop")
        if l1[i] > l1[i + 1]:
            print(i, ' ', l1[i], '', l1[i + 1])
            l1[i + 1], l1[i] = l1[i], l1[i + 1]

print(l1)

# let us reset l1 back
l1 = [1, 2, 3, 4, 6, 5]
i = 0
j = 0
for j in range(len(l1) - 1):
    flag = 0
    for i in range(len(l1) - 1):
        print("2nd approach inner-loop")
        if l1[i] > l1[i + 1]:
            print(i, ' ', l1[i], '', l1[i + 1])
            l1[i + 1], l1[i] = l1[i], l1[i + 1]
            flag = 1
    if flag == 0:  # if there is no change in list then list was already sorted
        break
print(l1)

# we can see flag makes inner loop do not run un-necessarily

####### Using Function

print("Using functions 1")
print("**********")
print(sorted(l1))  # returning sorted list

print("Using functions 2")
print("**********")
l1.sort()  # sort in place
print(l1)

# Sorting a nested list with dictionary

print("Sorting a nested list ")
print("**********")


l1 = [{'name': 'john', 'age': 88}, {'name': 'smith', 'age': 34}, {'name': 'will', 'age': 45},
      {'name': 'mike', 'age': 23}]

print(l1)

# sorting by age
sortfunction = lambda x: x['age']

newl1 = sorted(l1, key=sortfunction)
print(newl1)

l1.sort(key=sortfunction)  # in-place sort

print(l1)

print("Sorting a string ")
print("**********")

s1 = "hardly any snow season in atlanta"

# string is immutable in python hence we can iterate like list and shuffle values within but we have to convert it to list first

l1=s1.split()
print(l1)
print('now it is in list format and you can follow steps mentioned above to sort it ')
print('once list is sorted, we can convert it back to string')
l1.sort()
s1 = ' '.join(l1)
print(s1)

