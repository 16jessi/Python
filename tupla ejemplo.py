a=(1,2,3)
b=(-1,0,2)
prod=0
l=[]
for i in range(len(a)):
    prod+=a[i]*b[i]
    l.append(prod)
print(l)