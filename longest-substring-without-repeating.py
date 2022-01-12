s= "fsd  lsdd fslkk jffsk fjskdf sljfs kd sldk fsd "
s=s.split()
print(s)
l1=[]
for i,v in enumerate(s):
    cnt=0
    for j,k in enumerate(v):
        if k in v[j+1:]:
            cnt=1
            break
    if cnt==0:
        l1.append(v)

print(l1)

print(max(l1,key=len))

