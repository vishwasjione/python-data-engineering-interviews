
l1=[3,4,6,7,8]

fun = lambda x: x*x
fltr = lambda x : x%2   # 0 is considered false and non zeros are considered true and false are filtered

mapoutput = map(fun,l1)
print(list(mapoutput))

fltrvalues = filter(fltr,l1)
print(list(fltrvalues))

