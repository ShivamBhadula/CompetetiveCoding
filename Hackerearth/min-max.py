length=int(input())
a=list(map(int,input().split()))
a.sort()
a= list(dict.fromkeys(a))
for i in range(len(a)-1,0,-1):
    a[i]=a[i]-a[i-1]
if a.count(min(a))==len(a):
    print('YES')
else:
    print('NO')