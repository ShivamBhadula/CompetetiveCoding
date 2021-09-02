import math
x,n=map(int,input().split())
if n==3:
    n=6
elif n==4:
    n=4
elif n==1:
    n=1
elif n==2:
    n=2
else :
    n=0
 
print((x**n)%10)