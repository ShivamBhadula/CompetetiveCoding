
from itertools import *
for m in range(int(input())):
    s=int(input())
    n=list(map(int,input().split()))
    count=0
    k=list(combinations(n,2))
    for i in range(len(k)):
        sum=0
        if k[i][0]!=k[i][1]:
            sum=k[i][0]+k[i][1]
            if sum%2==0:
                count+=1
    print(count)