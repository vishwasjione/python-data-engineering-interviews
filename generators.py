
gen = (i for i in range(5))

print(type(gen))
print(tuple(gen))
print(list(gen))
print(list(range(4)))

for i in gen:
    print(i)