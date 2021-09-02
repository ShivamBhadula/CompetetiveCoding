import math
n=input().split(' ')
s=int(n[0])
t=int(n[1])
a=list(input().split(' '))
for i in range(1,s):
       a[i]=int(a[i])+int(a[i-1])
a.insert(0,0)
for j in range(t):
   c=input().split(' ')
   l=int(c[0])
   r=int(c[1])
   mean=0
   mean=(int(a[r])-int(a[l-1]))//(r-l+1)
   print(mean)