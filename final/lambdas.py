
# filter

l1=[1,3,5,6,7,8]

evenlist= list(filter(lambda x:x%2,l1)) # filter applies on each item and return only those items where it is true
print(evenlist)

# map

evenlist= list(map(lambda x:x%2,l1))  # map function applies on lambda on each item and return the value
print(evenlist)

# sorted
l1=[[1,4],[6,2],[-8,-9]]
l1.sort(key=lambda x:x[0])
print(l1)

l1=[3,5,6,7]
evenl1= [x for x in l1 if x%2==0]
print(evenl1)