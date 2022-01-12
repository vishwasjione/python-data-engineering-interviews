s = "abbabaaaabba"

fc = None
cnt = 1
store={}
i=0
while i < len(s):
    value = i
    for j in range(value + 1, len(s)):
        if s[i] == s[j]:
            cnt += 1
            i += 1
        else:
            break
    store.update({s[i]*cnt:cnt})
    cnt = 1
    i+=1

print(store)

# while i < range(len(s)):
