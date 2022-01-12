
# on list
l1=[2,4,6,7,8,9]
newlist =[x for x in l1 if x%2]
print(newlist)

l1=[[2,4],[6,7],[8,9]]
newlist =[x for x in l1 if x[1]%2]
print(newlist)

l1=[(2,4),(6,7),(8,9)]
newlist =[x for x in l1 if x[1]%2]
print(newlist)

# on tuple

t1=(2,4,6,7,8,9)
newtuple =[x for x in t1 if x%2]
print(newtuple)

t1=[(2,4),(6,7),(8,9)]
newtuple =[x for x in t1 if x[1]%2]
print(newtuple)

# on dict

dict1={"one":1,"two":2,"three":3,"four":4,"five":5}
newdict={ (a,b) for (a,b) in dict1.items() if b%2}
print(newdict)
print(dict(newdict))

