l1 = [4, 3, 8, 5, 9, 3]

# 1st way of doing it
def eq(l1):
    sum_left = l1[0]
    sum_right = sum(l1) - l1[0]
    initial_diff = abs(sum_right - sum_left)

    for i in range(1, len(l1) - 1):
        print('sum left-',sum_left, 'sum right', sum_right)
        sum_left += l1[i]
        sum_right -= l1[i]
        current_dif = abs(sum_right - sum_left)

        if current_dif < initial_diff:
            initial_diff = current_dif
            index = i
    return 'Least Difference-' + str(initial_diff) + ' at index-' + str(index)

print(eq(l1))

# 2nd way of doing it

l1 = [4, 3, 8, 5, 9, 3]

sumdiv2 = sum(l1)/2
total = 0
print('mid point value is -',sumdiv2)
for i,v in enumerate(l1):
    total+=v
    if total==sumdiv2:
        break
    if total>sumdiv2:
        break

if i==0:
    print("mid point index is -", i)

if abs(sumdiv2-l1[i])>abs(sumdiv2-l1[i-1]):
    print("mid point index is -", i-1)
else:
    print("mid point index is -", i)


