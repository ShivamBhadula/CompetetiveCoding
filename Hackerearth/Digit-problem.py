n=list(input().split(' '))
s=int(n[1])
n=n[0]
final=""
for i in n:
    if i!='9' and s>0 :
        final+='9'
        s-=1
    else :
        final+=i
print(final)