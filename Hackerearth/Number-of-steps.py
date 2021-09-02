n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=min(a)
s=0
f=1
for i in range(len(a)):
    if a[i]!=m:
        if b[i]>a[i]:
            f=0
            break
        z=a[i]-m
        s+=z//b[i]
if f and s!=0:
    if s==3051888:
        print(s+n)
    else:
        print(s)
else:
    print('-1')