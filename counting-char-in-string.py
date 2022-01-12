
# Cunting of characters

def countchar(s):

    list1=list(s)
    dictcounts={}
    for i in [x for x in list1 if x!=' ']:
        if i not in dictcounts:
            dictcounts[i]=1
        else:
            dictcounts[i]+=1

    dictcountsnoduplicates= {(a,b) for (a,b) in dictcounts.items() if b>1}
    print(dictcountsnoduplicates)
    print(dictcounts)

s = 'vishwas guptA'
news= s.upper()
countchar(s)


# true if any value is negative
def negative_check(l):

    if any(x for x in l if x<0):
        return True
    else:
        return False


print(negative_check([3,5,-6]))
print(negative_check([3,5,6]))


list1=[1,3,4]
tuple1=(2,4,5,6,6)

print(tuple1.index(4))
print(tuple1.count(6))



# find even numbers only in list
list1=[2,4,5,6,8]
list2=[x for x in list1 if x%2==0]
print(list2)



