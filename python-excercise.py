A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)

print(A0)
print(A1)
A2 = sorted([i for i in A1 if i in A0])
print(A2)

A3 = sorted([A0[s] for s in A0])
print(A3)

A4 = [i for i in A1 if i in A3]
print(A4)

A5 = {i:i*i for i in A1}

print(A5)

A6 = [[i,i*i] for i in A1]

print(A6)

def f(x,l=[]):
    for i in range(x):
        print(i)
        print(l)
        l.append(i*i)
    print(l)

# f(2)
# f(3,[3,2,1])
f(3)