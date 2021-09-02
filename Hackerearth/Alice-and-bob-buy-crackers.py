from itertools import *
n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(1,n+1):
    k=list(combinations(l,i))
    for i in k:
        if sum(i)%2==0:
            r.append(sum(i))
print(len(set(r)))