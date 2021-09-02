size=int(input())
l1=list(map(int,input().split()))
f=l1[0]
a=3
b=4
c=5
s=l1[1]
try:
    t=l1[2]
except:
    t=0
for i in range(3,size):
    if i==a:
        f+=l1[i]
        a+=3
    elif i==b:
        s+=l1[i]
        b+=3
    elif i==c:
        t+=l1[i]
        c+=3
print(f,s,t)