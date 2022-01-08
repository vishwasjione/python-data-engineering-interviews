
s = "abc dd kd lskd oabc ksl abc klakabc kf abc"

# 1st way
print(s.count("abc"))

# 2nd day

a= "abc"
cnt = [1 for x in s.split() if x==a]
print(sum(cnt))

# 3rd day

a= "abc"
cnt = [x==a for x in s.split()]
print(sum(cnt))