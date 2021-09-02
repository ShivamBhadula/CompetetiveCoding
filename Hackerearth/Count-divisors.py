t=list(input().split(' '))
l=int(t[0])
r=int(t[1])
k=int(t[2])
count=0
for l in range(l,r+1):
    if l%k==0:
        count+=1
print(count)
    