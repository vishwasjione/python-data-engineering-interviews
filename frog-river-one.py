
n = 5


dct1 = {}
for i in range(1, n + 1):
    dct1.update({i: 0})

print(dct1)
print('total leaf at this point in time is-',sum(dct1.values()))
#
tm1 = [1, 3, 1, 4, 2, 3, 5, 3, 2, 4, 3, 2]
#
# # first method
for i, v in enumerate(tm1):
    dct1.update({v: 1})
    print(dct1)
    if sum(dct1.values()) == 5:
        print("frog can cross at -", i)
        break

