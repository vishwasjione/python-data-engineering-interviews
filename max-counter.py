l1 = [3, 4, 4, 6, 1, 4, 4]
counter=[0]*(len(l1)-1)
maxcounter=0

addmax = lambda x : x +maxcounter
print(counter)
for v in l1:
    if v!=6:
        val=counter[v-1]
        counter[v-1]=val+1
        print(v,'-->',counter)
    else:
        print('max counter -',max(counter))
        counter=[x+max(counter) for x in counter if x!=max(counter)]
        print('new counter-', counter)


print((counter))